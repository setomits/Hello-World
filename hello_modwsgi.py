# -*- coding: utf-8 -*-

from webob import Request, Response

class MyApp(object):
    def __call__(self, environ, start_response):
        self.req = Request(environ)
        self.resp = Response()
        self.start_response = start_response

        return self._main()

    def _main(self):
        if self.req.POST:
            meth = 'POST'
            var1, var2 = (self.req.POST.get(k, u'') for k in ('var1', 'var2'))
        else:
            meth = 'GET'
            var1, var2 = (self.req.GET.get(k, u'') for k in ('var1', 'var2'))
        o = u'Method: "%s", var1: "%s", var2: "%s"' % (meth, var1, var2)

        self.resp.body = o.encode('utf-8', 'ignore')
        self.start_response(self.resp.status, self.resp.headerlist)

        return self.resp.body

application = MyApp()
