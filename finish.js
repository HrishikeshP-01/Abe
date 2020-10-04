let $=require('jquery');
const {spawn} = require('child_process');

$('#create-bot').on('click',()=>{
    const python = spawn('python',['fileCreator.py'])
})


