let debug =true
debug = debug ? console.log.bind(console)  : function () {};

let url_string = window.location.href; //window.location.href
let url = new URL(url_string);
let c = url.searchParams.get("uuid");

function exam_info() {
    $.ajax({
        url: '/ajax/exam_info/',
        data: {
            'uuid': c
        },
        dataType: 'json',
        success: function (data) {
            if (!data.error) {
                rander(data);
            }
        }
    });
}


function post_answer(json) {
    $.ajax({
        type: "POST",
        url: '/ajax/post_answer/',
        data: JSON.stringify(json),
        dataType: 'json',
        success: function (data) {
            if (!data.error) {
                //rander(data);
            }
        }
    });
}


function rander(json){
    if(!json.error){
        let container=document.querySelector('div.container');
        let ol=document.createElement('ol');
        container.insertBefore(ol,null);
        for(let quiz of json.body.quiz){
            let div=document.createElement('div');
            div.className='quiz';
            ol.insertBefore(div,null);
            let li=document.createElement('li');
            li.innerText=quiz.name;
            div.insertBefore(li,null);
            let ul=document.createElement('ul');
            div.insertBefore(ul,null);
            for(let option of quiz.option){
                li=document.createElement('li');
                ul.insertBefore(li,null);
                let label=document.createElement('label');
                label.setAttribute('for',option.name);
                label.innerText=option.name;
                li.insertBefore(label,null);
                let input=document.createElement('input');
                input.id=option.name;
                input.type=quiz.type;
                //input.value=option.name;
                li.insertBefore(input,null);
            }
        }
        if(json.body.status==1){
            let date=new Date(json.body.endTime)
            let endTime_utc =  Date.UTC(date.getUTCFullYear(), date.getUTCMonth(), date.getUTCDate(),
                date.getUTCHours(), date.getUTCMinutes(), date.getUTCSeconds());
            let p=document.createElement('p');
            p.innerText='笔试截止时间: '+new Date(endTime_utc);
            container.insertBefore(p,container.lastChild);
            let span=document.createElement('span');
            span.innerText='倒计时: ';
            container.insertBefore(span,container.lastChild);
            span=document.createElement('span');
            container.insertBefore(span,container.lastChild);
            date=new Date();
            let now_utc =  Date.UTC(date.getUTCFullYear(), date.getUTCMonth(), date.getUTCDate(),
                date.getUTCHours(), date.getUTCMinutes(), date.getUTCSeconds());
            let countdown=endTime_utc-now_utc;
            let interval=setInterval(function () {
                span.innerText=Math.floor(countdown/1000);
                if(countdown<=1000&&countdown>=-1000){
                    finishExam();
                    clearInterval(interval);
                }
                else if(countdown<=1000){
                    clearInterval(interval);
                }
                countdown-=1000;
            },1000);
        }
        else if(json.body.status==2){
            correct(json);
        }
    }
}


function finishExam() {
    let json={
        'uuid': c,
        'quiz':[]
    };
    let quizElemList=document.querySelectorAll('div.quiz');
    for(let quizElem of quizElemList){
        let optionElemList=quizElem.querySelectorAll('input');
        quiz={
            'name': quizElem.querySelector('li').innerText,
            'type': optionElemList[0].getAttribute('type'),
            'correct': false,
            'answer': []
        };
        for(let optionElem of optionElemList){
            debug(optionElem.value);
            if(optionElem.checked){
                quiz['answer'].push(optionElem.value);
            }
        }
        json['quiz'].push(quiz);
    }
    post_answer(json);
}


function correct(json){
    let userAnswer=JSON.parse(json.body.userAnswer);
    for(let quiz of userAnswer){
        let quizElemList=document.querySelectorAll('div.quiz');
        for(let quizElem of quizElemList){
            if(quizElem.firstChild.innerText==quiz.name){
                let optionList=quizElem.lastChild.childNodes;
                debug(optionList.length);
                for(let answer of quiz.answer){
                    debug(answer);
                    for(let option of optionList){
                        debug(option.firstChild.innerText);
                        if(quiz.type=='radio' || quiz.type=='checkbox'){
                            let checkMark=document.createElement('span');
                            if(option.firstChild.innerText==answer){
                                option.lastChild.checked=true;
                                checkMark.innerHTML='&#10004;';
                                quizElem.insertBefore(checkMark,quizElem.lastChild);
                                break;
                            }
                            else if(option==optionList.lastChild) {
                                checkMark.innerHTML='&#10006;';
                                quizElem.insertBefore(checkMark,quizElem.lastChild);
                            }
                        }
                        else if(quiz.type=='text'){

                        }
                    }
                }
                break;
            }
        }
    }
}