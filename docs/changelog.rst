----
News
----

1.2.7
-----
* Fix for mocking proxy objects. Worked in 1.2.5 but broken in 1.2.6 by the
  change to allow mocking static methods. Reported by Randy Syring.
* bugfix: ``mock_show_attrs`` was immutable after initialization because the
  ``mock_`` prefix was accidentally left off in ``Mock.__setattr__`` (Yusuke
  Muraoka)

1.2.6
-----
* Allow changing the tracker on a mock object once it's been set (James Brady)
* Support doctest use case (Israel Tsadok)
* Fix issue 1: setting mock_returns_iter on existing Mock object (kenmacd)
* Fix issue 2: static methods become unbound methods after mock + restore

1.2.5
-----
* Deprecate ``MockTracker``. ``TraceTracker`` should be used instead.

1.2.4
-----
* Fix show_attrs=True bug (Kendrick Shaw)

1.2.3
-----

* Explicitly passing ``tracker=None`` to the ``Mock`` constructor now
  suppresses tracking. If ``tracker`` is not passed it will still use
  ``Printer(sys.stdout)`` as before.

1.2.2
-----

* Added ``MinimockOutputChecker`` which normalizes whitespace in function call
  traces; ``TraceTracker`` now uses this instead of ``doctest.OutputChecker``
  (Ben Finney)

1.2.1
-----

* Allow mocking of built-in functions.

1.2
---

* Added ``TraceTracker``, a better ``Tracker`` to use with unittests (James Brady)

1.1
---

* Added ``MockTracker`` for use with unittests rather than doctests (James Brady)

1.0
---

* Fixed setting special attributes like ``mock_returns`` on
  already-created Mock objects (Toby White)

* Separated out printing to a class that accepts call information
  and provided an implementation that prints calls to a file.

0.9
---

* Added ``show_attrs``

0.8
---

First official release.
