let debug =true
debug = debug ? console.log.bind(console)  : function () {};
let optionCount=1;

function  insertGenre(e) {
    //==other
        if(e.target.value=='3'){
            let input=document.createElement('input');
            //input.type='text';
            //input.setAttribute('value','');
            e.target.parentElement.insertBefore(input, e.target.nextSibling);
        }
}

function  insertOption(e) {
    optionCount++;
    let newOption=e.target.parentElement.cloneNode(true);
    newOption.innerHTML=newOption.innerHTML.replace(/(option|选项)\d{1,2}/g,'$1'+optionCount);
    debug(newOption.innerHTML);
    e.target.parentElement.parentElement.insertBefore(newOption,e.target.parentElement.parentElement.lastChild);
    debug(e.target.parentElement.parentElement);
}

function insertButton(e) {
    let option1=document.querySelector('#option1');
    //!=text
    if(e.target.value!='3') {
        option1.nextElementSibling.nextElementSibling.addEventListener('click', insertOption);
        option1.previousElementSibling.innerText="选项1: ";
        option1.nextElementSibling.style.display='inline-block';
        option1.nextElementSibling.nextElementSibling.style.display='inline-block';
    }
    else{
        option1.previousElementSibling.innerText="答案: ";
        option1.nextElementSibling.style.display='none';
        option1.nextElementSibling.nextElementSibling.style.display='none';
    }
}