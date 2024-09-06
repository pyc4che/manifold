from core.flask import _flask

wsgi = _flask

def main():
    try:
        wsgi.run()
    
    except Exception as _:
        print(f'Enable to start Server! \@-@/ \n    {_}')


if __name__ == '__main__':
    main()
