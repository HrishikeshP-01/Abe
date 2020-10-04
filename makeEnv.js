let $ = require('jquery')
let fs = require('fs')
let filename='.env'

$('#make-env').on('click',()=>{
    let DT=$('#DT').val();
    let DG=$('#DG').val();
    console.log(DT);
    console.log(DG);
    entry="DISCORD_TOKEN = "+DT+"\nDISCORD_GUILD = "+DG+"\n";

    fs.appendFileSync('.env',entry)
    window.location.href="Finish.html";
})