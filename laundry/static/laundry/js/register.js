(function () {
    let input = '';
    let dots = document.querySelectorAll('.dot'), numbers = document.querySelectorAll('.number');
    let confirmationInput = '';
    let isConfirming = false;

    dots = Array.prototype.slice.call(dots);
    numbers = Array.prototype.slice.call(numbers);

    function resetDots() {
        dots.forEach(function (dot) {
            dot.className = 'dot';
        });
    }

    function handlePasswordSubmission() {
        if (isConfirming) {
            if (input === confirmationInput) {
                document.getElementById('username').value = document.getElementById('editableContent').innerText;
                console.log(document.getElementById('username').value);

                fetch('/register/', {
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
                    resetDots();
                    input = '';
                    confirmationInput = '';
                    isConfirming = false;
                }, 900);
                setTimeout(function () {
                    document.body.className = '';
                }, 1000);
            } else {
                document.getElementById('info_box').innerText = 'Passwords do not match. Please try again.';
                resetDots();
                input = '';
                confirmationInput = '';
                isConfirming = false;
            }
        } else {
            isConfirming = true;
            document.getElementById('info_box').innerText = 'Please confirm your password.';
            resetDots();
        }
    }

    numbers.forEach(function (number, index) {
        number.addEventListener('click', function () {
            number.className += ' grow';
            if (!isConfirming) {
                input += index + 1;
                dots[input.length - 1].className += ' active';
            } else {
                confirmationInput += index + 1;
                dots[confirmationInput.length - 1].className += ' active';
            }

            if (input.length >= 4 && (isConfirming ? confirmationInput.length >= 4 : true)) {
                handlePasswordSubmission();
            }

            setTimeout(function () {
                number.className = 'number';
            }, 1000);
        });
    });
}());
