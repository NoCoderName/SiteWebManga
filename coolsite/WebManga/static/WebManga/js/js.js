function checkCheckbox() {
    var checkbox = document.getElementById("add_post");
    var manga_pk = document.post.manga_pk.value;
    var user_name = document.post.user_name.value;
  
    if (checkbox.checked) {
      add_recording(manga_pk, user_name);
    } else {
      // Если чекбокс не отмечен, ничего не делать или вывести предупреждение
    }
  }
  
  document.addEventListener("click", function(event) {
    if (event.target.id === "add_post") {
      checkCheckbox();
    }
  });