// alert('ok')
$(document).ready(function () {
    //   类型 style_id
    // 排序方式 sort
    // 页码  page
    var params ={
        "style_id" : 1,
        "sort":2,
        "page":1
    };
    $.get('/list',params,function (data) {
        if (data.errcode == '200'){
            infolist = data.goodsdata;
            for(var i=0;i<infolist.length;i++){
                // alert(infolist[i].name);
                var li=
			   '<li class="gl-item"> <em class="icon_special tejia"></em> <div class="Borders"> <div class="img"><a href="/detail/{{data_obj.id}}"><img src="/static/products/p_2.jpg" style="width:220px;height:220px"></a></div> <div class="Price"><b>'+infolist[i].real_price+'</b><span>'+infolist[i].unite+'</span></div> <div class="name"><a href="/detail/{{data_obj.id}}">'+infolist[i].name+'</a></div> <div class="Shop_name"><a href="#">三只松鼠旗舰店</a></div> <div class="p-operate"> <a href="#" class="p-o-btn Collect"><em></em>收藏</a> <a href="#" class="p-o-btn shop_cart"><em></em>联系我们</a> </div> </div> </li>'

                $('.goodslist').append(li)

            }

        }

    })
})