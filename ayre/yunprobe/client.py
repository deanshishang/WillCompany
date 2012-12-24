#!/usr/bin/env python
import sys
from client.application import app
if __name__ == "__main__":
	app.parseArguments(sys.argv)
	app.initialize()
	app.run()
	app.finalize()
