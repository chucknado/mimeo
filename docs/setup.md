## Setting up Mimeo

Mime requires Python 3.6 or higher to run. It also uses a couple of third-party libraries that you must install on your system. The libraries can be installed with short one-line pip commands.

This is a one-time only setup.

* [Installing Python 3.6 or higher](#installing-python-3-6-or-higher)
* [Installing requests](#installing-requests)
* [Installing arrow](#installing-arrow)

After installing the required libraries on your system, you can install and configure Mime.

* [Installing Mime](#installing-mime)
* [Configuring Mime](#configuring-mime)

To learn how to use the tool, see [Using Mime](https://github.com/chucknado/mime/blob/master/docs/using-mime.md).


### Installing Python 3.6 or higher

Go to [http://www.python.org/download/](http://www.python.org/download/) and install the latest stable production version of Python 3 for your operating system.

You can test the installation by running `python3 --version` on the command line. It should give you the Python version number.

### Installing requests

The requests library simplifies making HTTP requests in Python. To learn more, see [Requests: HTTP for Humans](http://www.python-requests.org/en/latest/). To install requests, run the following command in your CLI:

```bash
$ pip3 install requests
```

### Installing arrow

The arrow library simplifies working with dates and times in Python. To learn more, see [Arrow: better dates and times for Python](http://arrow.readthedocs.io/en/latest/). To install arrow, run the following command in your CLI:

```bash
$ pip3 install arrow
```


### Installing Mime

1. Go to [https://github.com/chucknado/mime](https://github.com/chucknado/mime), click the green **Clone or Download** button on the right side, and choose **Download ZIP**.

2. Unzip and copy the folder to a folder that's easy to access from the command line. Example: **/Users/jdoe/tools/mime**.

3. You'll run the app from the command line so you should keep the path short. To get to the tool from the command line, you'd use the following command:

    ```bash
    $ cd tools/mime
    ```


### Configuring Mime

You have to be a Zendesk Support agent or administrator to use Mime.

1. In the **mime** application folder, open the **credentials.txt** file in the **basic_auth** folder.

2. On the first line, add your Zendesk Support username (email) and password, separated by a colon. Example:

	`jdoe@example.com:pa$$w0rd`

3. Save **credentials.txt**.

4. In Zendesk Support, click the Admin icon in the sidebar, then select **Channels** > **API**, and make sure **Password Access** is enabled in the settings. If you don't have permissions to do this, ask an admin to check for you.

 	<img src="https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gs_api_pwd_enabled.png" width="380px">


You should be good to go. To learn how to use the tool, see [Using Mime](https://github.com/chucknado/mime/blob/master/docs/using-mime.md).

