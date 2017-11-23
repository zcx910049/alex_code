class UrlPathRecordMiddleware(object):
    """用户访问url地址记录中间件类"""
    exclude_path = ['/user/login/','/user/register/','/user/logout/']
    # ajax发起的请求也不记录 request.is_ajax() 返回值为true或false
    # http://127.0.0.1:8001/user/address/?a=1 /user/address/

    def process_view(self,request,view_func,*view):
        """记录用户访问的地址"""
        if request.path not in UrlPathRecordMiddleware.exclude_path and not request.is_ajax():
            # 记录这个地址
            request.session['pre_url_path'] = request.path
