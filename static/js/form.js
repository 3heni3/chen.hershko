function validateForm() {
    let id_ = document.forms["ContactUsForm"]["id"].value;
    if (id_.length != 9) {
        alert('ID must be 9 digits');
        return false;
    }
    let isIDNum = /^\d+$/.test(id_);
    if (!isIDNum) {
        alert('ID must contain digits only');
        return false;
    }

    let phone = document.forms["ContactUsForm"]["phone"].value;
    if (phone.length != 10) {
        alert('Phone must be 10 digits');
        return false;
    }
    let isPhoneNum = /^\d+$/.test(phone);
    if (!isPhoneNum) {
        alert('Phone must contain digits only');
        return false;
    }

  }