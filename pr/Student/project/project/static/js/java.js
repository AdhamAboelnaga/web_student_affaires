
// Below function Executes on click of login button.
function Valid() {
    var name = document.getElementById("username");
    var password = document.getElementById("password");
    if (name.value == "" && password.value == "") 
    {
      alert("Please Login");
      return false;
    }
    else if (name.value == "" || password.value.length < 6) 
    {
      alert("Please Enter valid Name or Password->(min 6 charachters)");
      return false;
    }
    else 
    {
      return true;
    }
  
  
  }
  
  
  // Fillter search function 
  function myFunction() {
  
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("info");
    tr = table.getElementsByTagName("tr");
  
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  
  
  }
  
  
  
  function DeleteStudentdept(id, rowID) {
    let x = confirm("Are you sure you want to delet this Student?");
    if (x == true) {
      $.ajax({
        type: 'POST',
        url: `deleted/` + id,
        data: { csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() },
        success: function () {
          var row = rowID.parentNode.parentNode.rowIndex;
          document.getElementById("info").deleteRow(row);
  
        }
      })
    }
  
  }
  
  
  function DeleteStudentgraduate(id, rowID) {
    let x = confirm("Are you sure you want to delet this Student?");
    if (x == true) {
      $.ajax({
        type: 'POST',
        url: `deleteg/` + id,
        data: { csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() },
        success: function () {
          var row = rowID.parentNode.parentNode.rowIndex;
          document.getElementById("info").deleteRow(row);
  
        }
      })
    }
  
  }
  

  
  function DeleteStudentView(id, rowID) {
    let x = confirm("Are you sure you want to delet this Student?");
    if (x == true) {
      $.ajax({
        type: 'POST',
        url: `deletev/` + id,
        data: { csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() },
        success: function () {
          var row = rowID.parentNode.parentNode.rowIndex;
          document.getElementById("info").deleteRow(row);
  
        }
      })
    }
  
  }
  
  
  
  