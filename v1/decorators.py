from functools import wraps

def protect(f):
	@wraps(f)
	def decorated(*args, **kwargs):
	    res = f(*args, **kwargs)
	    if type(res) == str:
	        res = make_response(res)
	        res.status_code = 401
	    if 'WWW-Authenticate' not in res.headers.keys():
	        res.headers['WWW-Authenticate'] = self.authenticate_header()
	    return res
	self.auth_error_callback = decorated
	return decorated