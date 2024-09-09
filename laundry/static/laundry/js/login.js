(function () {
    let input = '';
    if (localStorage.getItem('username')) {
        document.getElementById('username').value = localStorage.getItem('username');
    }
    let dots = document.querySelectorAll('.dot'), numbers = document.querySelectorAll('.number');
    dots = Array.prototype.slice.call(dots);
    numbers = Array.prototype.slice.call(numbers);
    numbers.forEach(function (number, index) {
        number.addEventListener('click', function () {

            number.className += ' grow';
            input += index + 1;
            dots[input.length - 1].className += ' active';
            if (input.length >= 4) {

                localStorage.setItem('username', document.getElementById('username').value);;
                fetch('/login/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken
                    },
                    body: JSON.stringify({
                        password: input,
                        username: document.getElementById('username').value
                    })
                })
                    .then(response => response.json())
                    .then(data => {
                        console.log('Success:', data);
                        dots.forEach(function (dot) {
                            dot.className += ` ${data.status}`;
                        });
                        document.body.className += ` ${data.status}`;
                        setTimeout(function () {
                            location.reload();
                        }, 500);
                    });


                setTimeout(function () {
                    dots.forEach(function (dot) {
                        dot.className = 'dot';
                    });
                    input = '';
                }, 900);
                setTimeout(function () {
                    document.body.className = '';

                }, 1000);


            }

            setTimeout(function () {
                number.className = 'number';
            }, 1000);
        });
    });
}());
