$(function() {
  $('#selectSI').on('change', function() {
     var selection = $(this).val();
     //alert(selection);
     switch(selection){
       case "1":  //Escenario (0, 1)
         $("#fdpUcpuS").show()
         $("#fdpUmemS").show() 
         $("#fdpUnetS").hide()
         $("#fdpVcpuS").hide()
         $("#fdpVmemS").hide() 
         $("#lambdaUnetS").hide()
         $("#muUnetS").hide()
         $("#sigmaUnetS").hide() 
         $("#lambdaVcpuS").hide()
         $("#muVcpuS").hide()
         $("#sigmaVcpuS").hide() 
         $("#lambdaVmemS").hide()
         $("#muVmemS").hide()
         $("#sigmaVmemS").hide() 
         $("#lambdaVMS").hide()
         $("#muVMS").hide()
         $("#sigmaVMS").hide() 
         break;
       case "2": //Escenario (0, 2)
         $("#fdpUnetS").show()
         $("#fdpUcpuS").hide()
         $("#fdpUmemS").hide() 
         $("#lambdaUcpuS").hide()
         $("#muUcpuS").hide()
         $("#sigmaUcpuS").hide() 
         $("#lambdaUmemS").hide()
         $("#muUmemS").hide()
         $("#sigmaUmemS").hide() 
         $("#lambdaVMS").hide()
         $("#muVMS").hide()
         $("#sigmaVMS").hide() 
         $("#lambdaVcpuS").hide()
         $("#muVcpuS").hide()
         $("#sigmaVcpuS").hide() 
         $("#lambdaVmemS").hide()
         $("#muVmemS").hide()
         $("#sigmaVmemS").hide() 
       break;
       case "3": //Escenario (0, 3)
         $("#fdpUnetS").show()
         $("#fdpUcpuS").show()
         $("#fdpUmemS").show() 
        // $("#lambdaUcpuS").hide()
        // $("#muUcpuS").hide()
        // $("#sigmaUcpuS").hide() 
        // $("#lambdaUmemS").hide()
        // $("#muUmemS").hide()
        // $("#sigmaUmemS").hide() 
         $("#lambdaVMS").hide()
         $("#muVMS").hide()
         $("#sigmaVMS").hide() 
         $("#lambdaVcpuS").hide()
         $("#muVcpuS").hide()
         $("#sigmaVcpuS").hide() 
         $("#lambdaVmemS").hide()
         $("#muVmemS").hide()
         $("#sigmaVmemS").hide() 
        break;
       case "4": //Escenario (1, 0)
         $("#fdpVMS").show()
         $("#fdpUnetS").hide()
         $("#fdpUcpuS").hide()
         $("#fdpUmemS").hide() 
         $("#lambdaUcpuS").hide()
         $("#muUcpuS").hide()
         $("#sigmaUcpuS").hide() 
         $("#lambdaUmemS").hide()
         $("#muUmemS").hide()
         $("#sigmaUmemS").hide() 
         $("#lambdaUnetS").hide()
         $("#muUnetS").hide()
         $("#sigmaUnetS").hide() 
         $("#lambdaVcpuS").hide()
         $("#muVcpuS").hide()
         $("#sigmaVcpuS").hide() 
         $("#lambdaVmemS").hide()
         $("#muVmemS").hide()
         $("#sigmaVmemS").hide() 
        //$("#lambdaVMS").hide()
         //$("#muVMS").hide()
         //$("#sigmaVMS").hide() 
        break;
       case "5": //Escenario (1, 1)
         $("#fdpVMS").show()
         $("#fdpUnetS").hide()
         $("#fdpUcpuS").show()
         $("#fdpUmemS").show() 
         //$("#lambdaUcpuS").hide()
         //$("#muUcpuS").hide()
         //$("#sigmaUcpuS").hide() 
         //$("#lambdaUmemS").hide()
         //$("#muUmemS").hide()
         //$("#sigmaUmemS").hide() 
         $("#lambdaUnetS").hide()
         $("#muUnetS").hide()
         $("#sigmaUnetS").hide() 
         $("#lambdaVcpuS").hide()
         $("#muVcpuS").hide()
         $("#sigmaVcpuS").hide() 
         $("#lambdaVmemS").hide()
         $("#muVmemS").hide()
         $("#sigmaVmemS").hide() 
        // $("#lambdaVMS").hide()
        // $("#muVMS").hide()
        // $("#sigmaVMS").hide() 
        break;

       case "6": //Escenario (1, 2)
         $("#fdpVMS").show()
         $("#fdpUnetS").show()
         $("#fdpUcpuS").hide()
         $("#fdpUmemS").hide()
         $("#lambdaUcpuS").hide()
         $("#muUcpuS").hide()
         $("#sigmaUcpuS").hide()
         $("#lambdaUmemS").hide()
         $("#muUmemS").hide()
         $("#sigmaUmemS").hide()
         $("#lambdaVcpuS").hide()
         $("#muVcpuS").hide()
         $("#sigmaVcpuS").hide() 
         $("#lambdaVmemS").hide()
         $("#muVmemS").hide()
         $("#sigmaVmemS").hide() 
        //$("#lambdaUnetS").hide()
         //$("#muUnetS").hide()
         //$("#sigmaUnetS").hide()
         //$("#lambdaVMS").hide()
         //$("#muVMS").hide()
         //$("#sigmaVMS").hide()
        break;

       case "7": //Escenario (1, 3)
         $("#fdpVMS").show()
         $("#fdpUnetS").show()
         $("#fdpUcpuS").show()
         $("#fdpUmemS").show()
         $("#lambdaVcpuS").hide()
         $("#muVcpuS").hide()
         $("#sigmaVcpuS").hide() 
         $("#lambdaVmemS").hide()
         $("#muVmemS").hide()
         $("#sigmaVmemS").hide() 
        //$("#lambdaUcpuS").hide()
         //$("#muUcpuS").hide()
         //$("#sigmaUcpuS").hide()
         //$("#lambdaUmemS").hide()
         //$("#muUmemS").hide()
         //$("#sigmaUmemS").hide()
         //$("#lambdaUnetS").hide()
         //$("#muUnetS").hide()
         //$("#sigmaUnetS").hide()
         //$("#lambdaVMS").hide()
         //$("#muVMS").hide()
         //$("#sigmaVMS").hide()
        break;
        
        case "8":  //Escenario (2, 0)
         $("#fdpVcpuS").show()
         $("#fdpVmemS").show() 
         $("#fdpUcpuS").hide()
         $("#fdpUmemS").hide() 
         $("#fdpUnetS").hide()
         $("#lambdaUnetS").hide()
         $("#muUnetS").hide()
         $("#sigmaUnetS").hide() 
         $("#lambdaVMS").hide()
         $("#muVMS").hide()
         $("#sigmaVMS").hide() 
         $("#lambdaUcpuS").hide()
         $("#muUcpuS").hide()
         $("#sigmaUcpuS").hide()
         $("#lambdaUmemS").hide()
         $("#muUmemS").hide()
         $("#sigmaUmemS").hide()
         break;
       
       case "9":  //Escenario (2, 1)
         $("#fdpVcpuS").show()
         $("#fdpVmemS").show() 
         $("#fdpUcpuS").show()
         $("#fdpUmemS").show() 
         $("#fdpUnetS").hide()
         $("#fdpVMS").hide()
         $("#lambdaUnetS").hide()
         $("#muUnetS").hide()
         $("#sigmaUnetS").hide() 
         $("#lambdaVMS").hide()
         $("#muVMS").hide()
         $("#sigmaVMS").hide() 
         $("#lambdaUcpuS").hide()
         $("#muUcpuS").hide()
         $("#sigmaUcpuS").hide()
         $("#lambdaUmemS").hide()
         $("#muUmemS").hide()
         $("#sigmaUmemS").hide()
         break;
      
       case "10":  //Escenario (2, 2)
         $("#fdpVcpuS").show()
         $("#fdpVmemS").show() 
         $("#fdpUcpuS").hide()
         $("#fdpUmemS").hide() 
         $("#fdpUnetS").show()
         $("#fdpVMS").hide()
         $("#lambdaUnetS").hide()
         $("#muUnetS").hide()
         $("#sigmaUnetS").hide() 
         $("#lambdaVMS").hide()
         $("#muVMS").hide()
         $("#sigmaVMS").hide() 
         $("#lambdaUcpuS").hide()
         $("#muUcpuS").hide()
         $("#sigmaUcpuS").hide()
         $("#lambdaUmemS").hide()
         $("#muUmemS").hide()
         $("#sigmaUmemS").hide()
         break;
 
       case "11":  //Escenario (2, 3)
         $("#fdpVcpuS").show()
         $("#fdpVmemS").show() 
         $("#fdpUcpuS").show()
         $("#fdpUmemS").show() 
         $("#fdpUnetS").show()
         $("#fdpVMS").show()
         $("#lambdaUnetS").hide()
         $("#muUnetS").hide()
         $("#sigmaUnetS").hide() 
         $("#lambdaVMS").hide()
         $("#muVMS").hide()
         $("#sigmaVMS").hide() 
         $("#lambdaUcpuS").hide()
         $("#muUcpuS").hide()
         $("#sigmaUcpuS").hide()
         $("#lambdaUmemS").hide()
         $("#muUmemS").hide()
         $("#sigmaUmemS").hide()
         break;

       case "12":  //Escenario (3, 0)
         $("#fdpVcpuS").show()
         $("#fdpVmemS").show() 
         $("#fdpUcpuS").hide()
         $("#fdpUmemS").hide() 
         $("#fdpUnetS").hide()
         $("#fdpVMS").show()
         $("#lambdaUnetS").hide()
         $("#muUnetS").hide()
         $("#sigmaUnetS").hide() 
         $("#lambdaVMS").hide()
         $("#muVMS").hide()
         $("#sigmaVMS").hide() 
         $("#lambdaUcpuS").hide()
         $("#muUcpuS").hide()
         $("#sigmaUcpuS").hide()
         $("#lambdaUmemS").hide()
         $("#muUmemS").hide()
         $("#sigmaUmemS").hide()
         break;

       case "13":  //Escenario (3, 1)
         $("#fdpVcpuS").show()
         $("#fdpVmemS").show() 
         $("#fdpUcpuS").show()
         $("#fdpUmemS").show() 
         $("#fdpUnetS").hide()
         $("#fdpVMS").show()
         $("#lambdaUnetS").hide()
         $("#muUnetS").hide()
         $("#sigmaUnetS").hide() 
         $("#lambdaVMS").hide()
         $("#muVMS").hide()
         $("#sigmaVMS").hide() 
         $("#lambdaUcpuS").hide()
         $("#muUcpuS").hide()
         $("#sigmaUcpuS").hide()
         $("#lambdaUmemS").hide()
         $("#muUmemS").hide()
         $("#sigmaUmemS").hide()
         break;

      case "14":  //Escenario (3, 2)
         $("#fdpVcpuS").show()
         $("#fdpVmemS").show() 
         $("#fdpUcpuS").hide()
         $("#fdpUmemS").hide() 
         $("#fdpUnetS").show()
         $("#fdpVMS").show()
         $("#lambdaUnetS").hide()
         $("#muUnetS").hide()
         $("#sigmaUnetS").hide() 
         $("#lambdaVMS").hide()
         $("#muVMS").hide()
         $("#sigmaVMS").hide() 
         $("#lambdaUcpuS").hide()
         $("#muUcpuS").hide()
         $("#sigmaUcpuS").hide()
         $("#lambdaUmemS").hide()
         $("#muUmemS").hide()
         $("#sigmaUmemS").hide()
         break;

      case "15":  //Escenario (3, 3)
         $("#fdpVcpuS").show()
         $("#fdpVmemS").show() 
         $("#fdpUcpuS").show()
         $("#fdpUmemS").show() 
         $("#fdpUnetS").show()
         $("#fdpVMS").show()
         $("#lambdaUnetS").hide()
         $("#muUnetS").hide()
         $("#sigmaUnetS").hide() 
         $("#lambdaVMS").hide()
         $("#muVMS").hide()
         $("#sigmaVMS").hide() 
         $("#lambdaUcpuS").hide()
         $("#muUcpuS").hide()
         $("#sigmaUcpuS").hide()
         $("#lambdaUmemS").hide()
         $("#muUmemS").hide()
         $("#sigmaUmemS").hide()
         break;
      default: //Escenario (0, 0)
         $("#fdpUcpuS").hide()
         $("#fdpUmemS").hide()
         $("#fdpUnetS").hide()
         $("#fdpVcpuS").hide()
         $("#fdpVmemS").hide()
         $("#lambdaUcpuS").hide()
         $("#fdpVMS").hide()
         $("#muUcpuS").hide()
         $("#sigmaUcpuS").hide()
         $("#lambdaUmemS").hide()
         $("#muUmemS").hide()
         $("#sigmaUmemS").hide() 
         $("#lambdaUnetS").hide()
         $("#muUnetS").hide()
         $("#sigmaUnetS").hide() 
         $("#lambdaVMS").hide()
         $("#muVMS").hide()
         $("#sigmaVMS").hide() 
         $("#lambdaVcpuS").hide()
         $("#muVcpuS").hide()
         $("#sigmaVcpuS").hide() 
         $("#lambdaVmemS").hide()
         $("#muVmemS").hide()
         $("#sigmaVmemS").hide() 

     }
  });
});

////////////// PARAMETERS ///////////////

$(function() {
  $('#fdpUcpu').on('change', function() {
     var fdp = $(this).val();
     //alert(fdp)
     switch(fdp){
       case "0":
         $("#fUniformUcpuS").show()
         $("#tUniformUcpuS").show()  
         $("#lambdaUcpuS").hide()
         $("#muUcpuS").hide()
         $("#sigmaUcpuS").hide()
         break;
       case "1":
         $("#lambdaUcpuS").show()
         $("#muUcpuS").hide()
         $("#sigmaUcpuS").hide()
         $("#fUniformUcpuS").hide()
         $("#tUniformUcpuS").hide()  
         break;
       case "2":
         $("#lambdaUcpuS").hide()
         $("#muUcpuS").show()
         $("#sigmaUcpuS").show()
         $("#fUniformUcpuS").hide()
         $("#tUniformUcpuS").hide()  
         break;
       default:
         $("#lambdaUcpuS").hide()
         $("#muUcpuS").hide()
         $("#sigmaUcpuS").hide()
         $("#fUniformUcpuS").hide()
         $("#tUniformUcpuS").hide()  
        break;

     }
  });
});

$(function() {
  $('#fdpUmem').on('change', function() {
     var fdp = $(this).val();
     //alert(fdp)
     switch(fdp){
       case "0":
         $("#fUniformUmemS").show()
         $("#tUniformUmemS").show()  
         $("#lambdaUmemS").hide()
         $("#muUmemS").hide()
         $("#sigmaUmemS").hide()
         break;
       case "1":
         $("#lambdaUmemS").show()
         $("#muUmemS").hide()
         $("#sigmaUmemS").hide()
         $("#fUniformUmemS").hide()
         $("#tUniformUmemS").hide()         
         break;
       case "2":
         $("#lambdaUmemS").hide()
         $("#muUmemS").show()
         $("#sigmaUmemS").show()
         $("#fUniformUmemS").hide()
         $("#tUniformUmemS").hide()         
         break;
       default:
         $("#lambdaUmemS").hide()
         $("#muUmemS").hide()
         $("#sigmaUmemS").hide()
         $("#fUniformUmemS").hide()
         $("#tUniformUmemS").hide()         
         break;

     }
  });
});

$(function() {
  $('#fdpUnet').on('change', function() {
     var fdp = $(this).val();
     switch(fdp){
      case "0":
         $("#fUniformUnetS").show()
         $("#tUniformUnetS").show()
         $("#muUnetS").hide()
         $("#sigmaUnetS").hide()
         $("#lambdaUnetS").hide()
         break;
      case "1":
         $("#lambdaUnetS").show()
         $("#muUnetS").hide()
         $("#sigmaUnetS").hide()
         $("#fUniformUnetS").hide()
         $("#tUniformUnetS").hide()
         break;
      case "2":
         $("#lambdaUnetS").hide()
         $("#muUnetS").show()
         $("#sigmaUnetS").show()
         $("#fUniformUnetS").hide()
         $("#tUniformUnetS").hide()
        break;
      default:
         $("#lambdaUnetS").hide()
         $("#muUnetS").hide()
         $("#sigmaUnetS").hide()
         $("#fUniformUnetS").hide()
         $("#tUniformUnetS").hide()
        break;

     }
  });
});

$(function() {
  $('#fdpVM').on('change', function() {
     var fdp = $(this).val();
     switch(fdp){
       case "0":
         $("#fUniformVMS").show()
         $("#tUniformVMS").show()
         $("#muVMS").hide()
         $("#sigmaVMS").hide()
         $("#lambdaVMS").hide()
         break;
       case "1":
         $("#lambdaVMS").show()
         $("#muVMS").hide()
         $("#sigmaVMS").hide()
         $("#fUniformVMS").hide()
         $("#tUniformVMS").hide()
         break;
       case "2":
         $("#lambdaVMS").hide()
         $("#muVMS").show()
         $("#sigmaVMS").show()
         $("#fUniformVMS").hide()
         $("#tUniformVMS").hide()
         break;
       default:
         $("#lambdaVMS").hide()
         $("#muVM").hide()
         $("#sigmaVM").hide()
         $("#fUniformVMS").hide()
         $("#tUniformVMS").hide()
         break;

     }
  });
});

$(function() {
  $('#fdpVcpu').on('change', function() {
     var fdp = $(this).val();
     //alert(fdp)
     switch(fdp){
       case "0":
         $("#fUniformVcpuS").show()
         $("#tUniformVcpuS").show()
         $("#lambdaVcpuS").hide()
         $("#muVcpuS").hide()
         $("#sigmaVcpuS").hide()
         break;
       case "1":
         $("#lambdaVcpuS").show()
         $("#muVcpuS").hide()
         $("#sigmaVcpuS").hide()
         $("#fUniformVcpuS").hide()
         $("#tUniformVcpuS").hide()
        break;
       case "2":
         $("#lambdaVcpuS").hide()
         $("#muVcpuS").show()
         $("#sigmaVcpuS").show()
         $("#fUniformVcpuS").hide()
         $("#tUniformVcpuS").hide()
        break;
       default:
         $("#lambdaVcpuS").hide()
         $("#muVcpuS").hide()
         $("#sigmaVcpuS").hide()
         $("#fUniformVcpuS").show()
         $("#tUniformVcpuS").show()
        break;

     }
  });
});

$(function() {
  $('#fdpVmem').on('change', function() {
     var fdp = $(this).val();
     //alert(fdp)
     switch(fdp){
       case "0":
         $("#fUniformVmemS").show()
         $("#tUniformVmemS").show()
         $("#lambdaVmemS").hide()
         $("#muVmemS").hide()
         $("#sigmaVmemS").hide()
         break;
       case "1":
         $("#lambdaVmemS").show()
         $("#muVmemS").hide()
         $("#sigmaVmemS").hide()
         $("#fUniformVmemS").hide()
         $("#tUniformVmemS").hide()
        break;
       case "2":
         $("#lambdaVmemS").hide()
         $("#muVmemS").show()
         $("#sigmaVmemS").show()
         $("#fUniformVmemS").hide()
         $("#tUniformVmemS").hide()
        break;
       default:
         $("#lambdaVmemS").hide()
         $("#muVmemS").hide()
         $("#sigmaVmemS").hide()
         $("#fUniformVmemS").show()
         $("#tUniformVmemS").show()           
         break;

     }
  });
});

