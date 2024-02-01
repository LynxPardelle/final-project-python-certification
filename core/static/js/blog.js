async function deleteBlog(id) {
  try {
    /* CSRF */
    let csrftoken = getCookie("csrftoken");
    let response = await fetch(`/blog/delete/${id}`, {
      method: "DELETE",
      headers: {
        "X-CSRFToken": csrftoken,
        "Content-Type": "application/json",
      },
    });
    if (response.ok) {
      window.location.href = "/blog";
    } else {
      alert("Failed to delete blog");
    }
  } catch (error) {
    console.error(error);
  }
}
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    let cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  console.log(cookieValue);
  return cookieValue;
}
async function searchBlog() {
  try {
    let input = document.getElementById("search").value;
    input = input.toLowerCase();
    window.location.href = `/blog/search/0/${input}`;
    /* let csrftoken = getCookie("csrftoken");
    let response = await fetch(`/blog/search/0/${input}`, {
      method: "GET",
      headers: {
        "X-CSRFToken": csrftoken,
        "Content-Type": "application/json",
      },
    });
    if (!response.ok) {
      alert("Failed to search blog");
    } */
  } catch (error) {
    alert(error.message);
  }
}
