MiniMock
========

..  contents::
    :depth: 1

--------------------
License & Repository
--------------------

MiniMock is by `Ian Bicking <http://blog.ianbicking.org>`_ with
substantial contributions by Mike Beachy, and is maintained by Josh
Bronson. It is licensed under an `MIT-style license
<http://bitbucket.org/jab/minimock/src/tip/docs/license.txt>`_.

It has a `bitbucket repository <http://bitbucket.org/jab/minimock/>`_
which you can clone with ``hg clone https://jab@bitbucket.org/jab/minimock/``,
download an archive of the tip from
`http://bitbucket.org/jab/minimock/get/tip.gz
<http://bitbucket.org/jab/minimock/get/tip.gz#egg=MiniMock-dev>`_,
or install from with ``easy_install MiniMock==dev``.
There is also a `Google Group <http://groups.google.com/group/minimock-dev>`_
for the development mailing list which can be emailed at
`minimock-dev@googlegroups.com <mailto:minimock-dev@googlegroups.com>`_.

------------
Introduction
------------

minimock is a simple library for doing Mock objects with doctest.
When using doctest, mock objects can be very simple.

Here's an example of something we might test, a simple email sender::

    >>> import smtplib
    >>> def send_email(from_addr, to_addr, subject, body):
    ...     conn = smtplib.SMTP('localhost')
    ...     msg = 'To: %s\nFrom: %s\nSubject: %s\n\n%s' % (
    ...         to_addr, from_addr, subject, body)
    ...     conn.sendmail(from_addr, [to_addr], msg)
    ...     conn.quit()

Now we want to make a mock ``smtplib.SMTP`` object.  We'll have to
inject our mock into the ``smtplib`` module::

    >>> smtplib.SMTP = Mock('smtplib.SMTP')
    >>> smtplib.SMTP.mock_returns = Mock('smtp_connection')

Now we do the test::

    >>> send_email('ianb@colorstudy.com', 'joe@example.com',
    ...            'Hi there!', 'How is it going?')
    Called smtplib.SMTP('localhost')
    Called smtp_connection.sendmail(
        'ianb@colorstudy.com',
        ['joe@example.com'],
        'To: joe@example.com\nFrom: ianb@colorstudy.com\nSubject: Hi there!\n\nHow is it going?')
    Called smtp_connection.quit()

Voila!  We've tested implicitly that no unexpected methods were called
on the object.  We've also tested the arguments that the mock object
got.  We've provided fake return calls (for the ``smtplib.SMTP()``
constructor).  These are all the core parts of a mock library.  The
implementation is simple because most of the work is done by doctest.

-----------------
Controlling Mocks
-----------------

Mock objects have several attributes, all of which you can set when
instantiating the object.  To avoid name collision, all the attributes
start with ``mock_``, while the constructor arguments don't.

``name``:
    The name of the object, used when printing out messages.  In the
    example above it was ``'smtplib.SMTP'``.

``returns``:
    When this object is called, it will return this value.  By default
    it is None.

``returns_iter``:
    Alternately, you can give an iterable of return results, like
    ``returns_iter=[1, 2, 3]``; on each subsequent call it will return
    the next value.

``returns_func``:
    If given, this will be called to get the return value.  In
    essence, this function will be the *real* implementation of the
    method.

``raises``:
    An exception (instance or class) that will be raised when this
    object is called.

``tracker``:
    An object which is notified every time the mock object is called or
    an attribute is set on it (assuming ``show_attrs`` is ``True``);
    defaults to a ``Printer`` to stdout. ``TraceTracker`` can instead be
    useful for non-doctest tests. Pass ``None`` to disable this behavior.

``show_attrs``:
    If this is true, every time a new attribute is set on the mock
    object the tracker will be notified. Otherwise attribute sets are
    silent, and only calls trigger notification.

So to create an object that always raises ValueError, do::

    >>> dummy_module = Mock('mylibrary')
    >>> dummy_module.invalid_func.mock_raises = ValueError

--------------
Creating Mocks
--------------

Every attribute of a mock object will itself be another mock object,
unless you specifically set it to something else.  For instance, you
can do::

    >>> from minimock import Mock
    >>> dummy_module = Mock('mylibrary')
    >>> dummy_module.CONSTANT = 1

Then the ``CONSTANT`` value will persist.  But you can also traverse
to whatever object you want, and you will get another mock object.

Another technique for creating a mock object is the ``mock(...)``
function.  This works like::

    >>> from minimock import mock
    >>> import os.path
    >>> mock('os.path.isfile', returns=True)

This looks up the ``os.path.isfile`` object, and changes it to a mock
object.  Any keyword arguments you give (like ``returns=True`` in this
example) will be used to create the mock object; you can also give a
``mock_obj`` keyword argument to pass in a mock object you've already
created.

This function looks in the calling function to figure out what to
replace (``os.path.isfile`` in the example).  You must import the
proper modules first.  Alternately you can pass in a dictionary like
``[locals(), globals()]`` for it to use for lookup.

To restore all the objects mocked with ``mock()``, use
``minimock.restore()`` (with no arguments; all the mocks are kept
track of).
