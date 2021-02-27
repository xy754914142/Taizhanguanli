$(function () {

    $('#shouye').removeClass('active');
    $('#update').removeClass('active');
    $('#taizhang').addClass('active');
    $('#complete_bt').click(function () {
        var token = $.cookie('csrftoken');
        var hobbies = document.getElementsByName('hobby');
        var value;
        for (i = 0; i < hobbies.length; i++) {
            if (hobbies[i].checked) {
                if (!value) {
                    value = hobbies[i].value;
                } else {
                    value += "," + hobbies[i].value;
                }
            }
        }
        if (value == '') {
            lightyear.loading('show');
            // 假设ajax提交操作
            setTimeout(function () {
                lightyear.loading('hide');
                lightyear.notify('请至少选择一台设备，请修改后再试~', 'danger', 100);
            }, 1e3)
        } else {
            $.ajax({
                url: '/completes.html',
                type: 'POST',
                data: {'values': value},
                dataType: 'JSON',
                headers: {'X-CSRFToken': token},
                success: function (args) {
                    if (args.status) {
                        console.log(args.status);
                        lightyear.loading('show');
                        // 假设ajax提交操作
                        setTimeout(function () {
                            lightyear.loading('hide');
                            lightyear.notify('提交完成,正在跳转~', 'success', 3000);
                        }, 1e3);
                        setTimeout('location.reload()', 2000);
                    } else {
                        lightyear.loading('show');
                        // 假设ajax提交操作
                        setTimeout(function () {
                            lightyear.loading('hide');
                            lightyear.notify('修改失败，请稍后再试~', 'danger', 100);
                        }, 1e3)
                    }
                }
            })
        }
    })
})