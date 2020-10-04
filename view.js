let $ = require('jquery')
let fs = require('fs')
let filename = 'Botresponses'
let sno=0

$('#add-to-list').on('click',()=>{
    let UQ=$('#UQ').val();
    let BR=$('#BR').val();
    let entry = UQ+":::"+BR+"\n";
    console.log(entry);

    fs.appendFileSync('Botresponses',entry);

    addEntry(UQ,BR);
})

function addEntry(UQ,BR){
    if(UQ && BR){
        sno++;
        let updateString='<tr><td>'+sno+'</td><td>'+UQ+'</td><td>'+BR+'</td></tr>';
        $('#response-table').append(updateString);
    }
}

function loadAndDisplayResponses(){
    //Check if file exists
    if(fs.existsSync(filename)){
        let data=fs.readFileSync(filename,'utf-8').split('\n')
        data.forEach((contact,index)=>{
            let [UQ,BR]=contact.split(':::');
            addEntry(UQ,BR);
        })
    }
    else{
        console.log("File Doesn't exist Creating new file");
        fs.writeFile(filename,'',(err)=>{
            if(err)
                console.log(err);
        })
    }
}

loadAndDisplayResponses()