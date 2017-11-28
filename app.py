#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '''
    <pre>
    m    m        ""#    ""#                 m     m               ""#        #
    #    #  mmm     #      #     mmm         #  #  #  mmm    m mm    #     mmm#
    #mmmm# #"  #    #      #    #" "#        " #"# # #" "#   #"  "   #    #" "#
    #    # #""""    #      #    #   #         ## ##" #   #   #       #    #   #
    #    # "#mm"    "mm    "mm  "#m#"         #   #  "#m#"   #       "mm  "#m##
 
    Dit is python in een docker container!
 
    * Dependency 'flask' is geinstalleerd
    * Port 5000 is opengezet in de container
    </pre>
    '''

@app.route('/test')
def test():
    return 'Oii'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
