$(document).ready(function() {

    $('#submit').click(function() {
        let res1 = true;
        let res2 = true;
        let res3 = true;
        let res4 = true;

        if (res1 == true && res2 == true && res3 == true && res4 == true) {
            $('#form-1').attr('onsubmit', 'return true'); // - разблокировка формы
        } else {
            $('#form-1').attr('onsubmit', 'return false'); // - переблокировка формы
            alert('Форма содержит некоректные данные! \nОтправка данных заблокирована');
        }
    });

});