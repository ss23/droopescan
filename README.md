# A CMS Scanning Tool.

Stable versions can be [found here](https://github.com/droope/droopescan/releases).

Usage:

<pre>
python droopescan.py scan drupal --url http://localhost/drupal-7.28
python droopescan.py scan silverstripe --url http://localhost/silverstripe
</pre>

You can get a full list of options by running:

<pre>
python droopescan.py --help
python droopescan.py scan --help
</pre>

# Dependencies.

In order to run this tool you need to install a few dependencies. These can be
installed by running the following command:

<pre>
pip install requirements.txt
</pre>

# Scan types.

Droopescan aims to be the most aggressive by default, while not overloading the
target server due to excessive requests. Due to this, by default, a large number
of requests will be made with four threads; you can increase this default by
using the `--threads` argument.

This tool is able to perform four kinds of tests:

* Plugin checks: Performs several hundred requests and returns a listing of all
plugins found to be installed in the target host.
* Theme checks: As above, but for themes.
* Version checks: Downloads several files and, based on the checksums of these
files, returns a list of all possible versions. 
* Interesting url checks: Checks for interesting urls (admin panels, readme
files, etc.)

# Authentication.

The application fully supports `.netrc` files and `http_proxy` environment
variables. 

You can set `http_proxy` and `https_proxy` variables. These allow you to
set a parent HTTP proxy, in which you can handle more complex types of
authentication (e.g. Fiddler, ZAP)

<pre>
export http_proxy='localhost:8080'
export https_proxy='localhost:8080'
python droopescan.py drupal --url http://localhost/drupal
</pre>

Another option is to use a .netrc file. An example `~/.netrc` file could look
as follows:

<pre>
machine secret.google.com
    login pedro.worcel@security-assessment.com
    password Winter01
</pre>

*WARNING:* By design, to allow intercepting proxies, this application allows
self-signed or otherwise invalid certificates.

# Output.

This application supports both "standard output", meant for human consumption,
or JSON, which is more suitable for machine consumption.

This can be controlled with the `--output` flag, and some sample JSON output
would look as follows:

<pre>
{
  "themes": {
    "is_empty": true,
    "finds": [
      
    ]
  },
  "interesting urls": {
    "is_empty": false,
    "finds": [
      {
        "url": "https:\/\/www.drupal.org\/CHANGELOG.txt",
        "description": "Default changelog file."
      },
      {
        "url": "https:\/\/www.drupal.org\/user\/login",
        "description": "Default admin."
      }
    ]
  },
  "version": {
    "is_empty": false,
    "finds": [
      "7.29",
      "7.30",
      "7.31"
    ]
  },
  "plugins": {
    "is_empty": false,
    "finds": [
      {
        "url": "https:\/\/www.drupal.org\/sites\/all\/modules\/views\/",
        "name": "views"
      },
      [...snip...]
    ]
  }
}
</pre>

# Testing

To run tests, some dependencies can be installed; running the following
commands will result in them being installed and the tests being ran:

<pre>
    apt-get install python-dev libxslt1-dev libxml2-dev
    pip install requirements_test.txt
    ./droopescan test
</pre>

Tests which interact with the internet can be ran with the following command:

<pre>
    ./droopescan test -i
</pre>
