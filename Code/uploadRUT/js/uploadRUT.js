$('.upload-btn').on('click',function(){
    $('#upload-file').click();
  })
$('#upload-file').on('change',function(){
  let files=$(this).get(0).files;
  let result= document.createElement('p');
  $('#result').html('RUT: '+files[0].name);
  $('#change').css("display", "none");
  $('#btnSiguiente').css("display", "inline-block");
  
})