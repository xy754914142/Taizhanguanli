$(function () {
    Set_select_type();
    Submit_bt();
})

function Set_select_type() {
    var d_t = $('#device_t').val();
    var select_1 = document.getElementById("select_id");
    for (i = 0; i < select_1.options.length; i++) {
        if (select_1.options[i].value == d_t) {
            select_1.options[i].selected = true;
        }
    }
}

function Submit_bt() {
    $('#submit').click(function () {
        var token = $.cookie('csrftoken');
        var editnumber = $('#editnumber').val() + '.html';
        var d_t = $('#device_t').val();
        var datas = {};
        datas['device_name'] = $('#device_name').val();
        datas['device_model'] = $('#device_model').val();
        datas['device_range'] = $('#device_range').val();
        datas['device_precision'] = $('#device_precision').val();
        datas['manufacturer'] = $('#manufacturer').val();
        datas['Commissioning_date'] = $('#Commissioning_date').val();
        datas['device_number'] = $('#device_number').val();
        datas['device_factory_number'] = $('#device_factory_number').val();
        datas['calibration_department'] = $('#calibration_department').val();
        datas['calibration_cycle'] = $('#calibration_cycle').val();
        datas['calibration_time'] = $('#calibration_time').val();
        datas['expire_time'] = $('#expire_time').val();
        datas['device_type'] = $('#select_id').val();
        datas['device_user_department'] = $('#device_user_department').val();
        datas['node'] = $('#node').val();
        var post_data = JSON.stringify(datas);
        if ($('#device_factory_number').val() == '') {
            lightyear.loading('show');
            // 假设ajax提交操作
            setTimeout(function () {
                lightyear.loading('hide');
                lightyear.notify('本厂编号不能为空，请修改后再试~', 'danger', 100);
            }, 1e3)
        } else {
            $.ajax({
                url: editnumber,
                type: 'POST',
                data: {'datas': post_data,'device_t':d_t},
                dataType: 'JSON',
                headers: {'X-CSRFToken': token},
                success: function (args) {
                    if (args.status) {
                        lightyear.loading('show');
                        // 假设ajax提交操作
                        setTimeout(function () {
                            lightyear.loading('hide');
                            lightyear.notify('修改成功~', 'success', 3000);
                        }, 1e3);

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
}