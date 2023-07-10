


function Login() {
    var username = $('#form3Example3').val()
    var password = $('#form3Example4').val()
    $("#password_error").html('')
    $("#username_error").html('')
    if (username === ''){
        $("#username_error").html('Username is required!')
        return;
    }

    if (password === ''){
        $("#password_error").html('Password is required!!')
        return;
    }
    var csrftoken = $('input[name=csrfmiddlewaretoken]').val()
    $.ajax({
            method: 'POST',
            url : '/login_process/',
            data : {
                'username':username,
                'password':password,
                 csrfmiddlewaretoken:csrftoken
            },
            success:function (response) {
                if (response.status === 'successful'){
                    setTimeout(()=>{location.href='/'} , 1500)

                    const Toast = Swal.mixin({
                      toast: true,
                      position: 'top-end',
                      showConfirmButton: false,
                      timer: 2000,
                      timerProgressBar: true,
                      didOpen: (toast) => {
                        toast.addEventListener('mouseenter', Swal.stopTimer)
                        toast.addEventListener('mouseleave', Swal.resumeTimer)
                      }
                    })

                    Toast.fire({
                      icon: 'success',
                      title: 'Signed in successfully'
                    })
                }else if (response.status === 'failed') {
                       $("#password_error").html('Password is not correct!!')
                       $("#username_error").html('Username is not correct!!')
                }
            }
        })



}




function CreateAccount() {
    var username = $('#form3Example3').val()
    var password = $('#form3Example4').val()
    var fullname = $('#form3Example1').val()
    var company_name = $('#form3Example2').val()
    $("#password_error").html('')
    $("#username_error").html('')
    $("#fullname_error").html('')
    $("#company_error").html('')

    if (username === ''){
        $("#username_error").html('Username is required!')
        return;
    }

    if (password === ''){
        $("#password_error").html('Password is required!!')
        return;
    }

    if (company_name === ''){
        $("#company_error").html('Password is required!!')
        return;
    }

    if (fullname === ''){
        $("#fullname_error").html('Password is required!!')
        return;
    }

    var csrftoken = $('input[name=csrfmiddlewaretoken]').val()
    $.ajax({
            method: 'POST',
            url : '/create_account/',
            data : {
                'username':username,
                'password':password,
                'fullname':fullname,
                'company_name':company_name,
                 csrfmiddlewaretoken:csrftoken
            },
            success:function (response) {
                if (response.status === 'successful'){
                    setTimeout(()=>{location.href='/login/'} , 1000)
                    alert('Create account was successful!')
                }else if (response.status === 'username already taken') {
                       $("#username_error").html('username already taken!')
                }
            }
        })



}



function Send_Request(id , el_id) {
        var csrftoken = $('input[name=csrfmiddlewaretoken]').val()
        var quantity = $(el_id).val()
        $.ajax({
            method: 'POST',
            url : '/order_request/',
            data : {
                'id':id,
                'quantity':quantity,
                 csrfmiddlewaretoken:csrftoken
            },
            success:function (response) {
                if (response.status === 'successful'){
                    Swal.fire(
                      'Order Request Sent!',
                      'You must wait until the order is confirmed.',
                      'success'
                    )
                }else if(response.status === 'no'){

                        Swal.fire({
                          icon: 'error',
                          title: 'Insufficient Inventory!',
                        })
                }else{
                    setTimeout(()=>{location.href='/login/'} , 10)
                    alert('You must be login!')
                }
            }
        })


}
