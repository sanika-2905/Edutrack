function showSection(id) {
  const sections = document.querySelectorAll('.section');
  sections.forEach(section => {
    section.style.display = 'none';
  });

  const selectedSection = document.getElementById(id);
  if (selectedSection) {
    selectedSection.style.display = 'block';
  }
}

function logout() {
  alert("Logging out...");
  window.location.href = "teacher_login.html";
}


  const modal = document.getElementById('loginModal');
  const btn = document.getElementById('teacherLoginBtn');
  const closeBtn = document.getElementById('closeModal');

  btn.onclick = () => {
    modal.style.display = 'block';
  };

  closeBtn.onclick = () => {
    modal.style.display = 'none';
  };

  window.onclick = (event) => {
    if(event.target === modal) {
      modal.style.display = 'none';
    }
  };

