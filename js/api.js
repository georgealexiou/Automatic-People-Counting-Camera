import fetch from 'node-fetch';

function fetch(date){
    const response = await fetch('https://api.github.com/users/github');
    const options = { year: '2-digit', month: '2-digit', day: '2-digit'};
    const americanDateTime = new Intl.DateTimeFormat('en-US', options).format;
}

const data = await response.json();

console.log(data);