$('#search_bt').click(function () {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();

    $.ajax({
        type:"POST",
        url:"/search/",
        data:{'search_text':$('#search_text').val(),'csrfmiddlewaretoken':csrf},// 注意csrf随机字符串，后台有固定的名字接收,这种方式是通过标签获取的对应值
        success:function (data) {
            console.log(data);
        }
    })
})