function someFunction(event){
    event.preventDefault();
    var form = document.forms["AgeForm"];

    day = Number.parseInt(form.elements['day'].value);
    month = Number.parseInt(form.elements['month'].value);
    year = Number.parseInt(form.elements['year'].value);

    console.log(day, month, year)

    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
    "day": day,
    "month": month,
    "year": year
    });

    var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
    };

    fetch("http://127.0.0.1:8000/computeAge/", requestOptions)
    .then(response => response.json())
    .then(result => document.getElementById('response').textContent = result.message)
    .catch(error => console.log('error', error));

    result
}