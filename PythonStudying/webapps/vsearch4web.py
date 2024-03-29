from flask import Flask, render_template, request, session, copy_current_request_context
from vsearch import search4letters
from threading import Thread
from time import sleep

from DBcm import UseDatabase, ConnectionError, CredentialError, SQLError
from checker import check_loggged_in


app = Flask(__name__)

app.config['dbconfig'] = {'host' : '127.0.0.1',
                'user' : 'vsearch',
                'password' : 'vsearchpasswd',
                'database' : 'vsearchlogDB', }
    

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out'


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        """ Log details of the web request and the results. """
        sleep(15)
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """ insert into log
                   (phrase, letters, ip, browser_string, results)
                   values
                   (%s, %s, %s, %s, %s)"""
            cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res, ))
            
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are ur results'
    results = str(search4letters(phrase, letters))
    try: 
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:
        print('*****Logging failed with this error: ', str(err))
    return render_template('result.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)


@app.route('/viewlog')
@check_loggged_in
def view_the_log() -> 'html':
    try: 
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """ select phrase, letters, ip, browser_string, results from log"""
            cursor.execute(_SQL)
            contests = cursor.fetchall()
        titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
        return render_template('viewlog.html',
                           the_title='View Log', 
                           the_row_titles=titles,
                           the_data=contests,)
    except ConnectionError as err:
        print('Is ur database switched on? Error: ', str(err)) 
    except CredentialError as err:
        print('User-id/Password issues. Error: ', str(err))
    except SQLError as err:
        print('Is ur query correct?  Error: ', str(err))
    except Exception as err:
        print('Something went wrong: ', str(err))
    return 'Error'


@app.route('/')
@app.route('/entry')
def entry_page() -> str:
    return render_template('entry.html',
                           the_title='Welcome to search4letters on th web!')


app.secret_key = 'YouWillNeverGuessMySecretKey'

if __name__ == '__main__':
    app.run(debug=True)
