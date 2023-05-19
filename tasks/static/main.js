function valid_check(sender, index) {
    if (sender.value === "") {
        if (index === 1) {
            sender.setCustomValidity('لطفا نام خود را وارد کنید');
        } else {
            sender.setCustomValidity('لطفا نام خانوادگی خود را وارد کنید');
        }
    }


}

function num2en(str) {
    const persianNum = ["۰","۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"];
    let phone = str;

    for (let i = 0; i < persianNum.length; i++) {
        phone = phone.replaceAll(persianNum[i], i);
    }
    return phone;

}

function phone_valid_check(sender) {
    if (sender.value === "") {
        sender.setCustomValidity('لطفا شماره تلفن خود را وارد کنید');
    }
    else if (sender.value.length !== 11) {
        sender.setCustomValidity('لطفا یک شماره تلفن معتبر ایرانی با الگوی خواسته شده وارد کنید');
    }
    else {
        const phone = num2en(sender.value+'');
        let reg = /09[0-9]{9}/i;
        if (!phone.match(reg)) {
            sender.setCustomValidity('لطفا یک شماره تلفن معتبر ایرانی با الگوی خواسته شده وارد کنید');
        }
    }

}

function email_valid_check(sender) {
    if (sender.value === "") {
        sender.setCustomValidity('لطفا ایمیل خود را وارد کنید');
    }
    else {
        let reg = /[a-zA-Z0-9.-_]+@[a-zA-Z.-]{2,}[.][a-zA-Z]{2,}/i;
        const email = sender.value + '';
        if (!email.match(reg)) {
            sender.setCustomValidity('لطفا ایمیل خود را بدرستی وارد کنید');
        }
    }

}

function form_click(){
    document.getElementById('submit_from').style.display = 'none';
    document.getElementById('submit_from_loading').style.display = 'block';
}

function empty_check(sender){
    if (sender.value!==""){
        sender.setCustomValidity('')
    }
    else {
        const type=sender.title;
        sender.setCustomValidity('لطفا '+type+' خود را وارد کنید')
    }
}