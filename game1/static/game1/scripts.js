

document.getElementById('search-btn').addEventListener('click', function () {
    const playerName = document.getElementById('player-name').value;
    const statsContainer = document.getElementById('stats-container');
    if (!playerName) {
      statsContainer.innerHTML = '<p>Please enter a Account Id.</p>';
      return;
    }
    //send get request to the server
    fetch('get_stats?account_id=' + playerName,
    {
      method: 'GET',
      headers: {
        application: 'application/json',
      },
    }).then(response => response.json())
    .then(data => {
      let player=data.stats;
      var profile=player.data.profile;
      sessionStorage.setItem('player', JSON.stringify({'playerName':playerName,'avatar':profile.avatar,'personaname':profile.personaname,'profileurl':profile.profileurl}));
      document.getElementById("avatar").src=profile.avatar;
      document.getElementById("personaname").innerHTML=profile.personaname;
      document.getElementById("profilelink").href=profile.profileurl;
    })
  });


  // document.getElementById('verify-stats-btn').addEventListener('click', function () {
  //   fetch('verify_stats',
  //     {
  //       method: 'GET',
  //       headers: {
  //         application: 'application/json',
  //       },
  //     })
  //     .then(response => response.json())
  //     .then(data => {
  //       // Display the response in the 'verification-result' div
  //       document.getElementById('verification-result').textContent = data.message;
  //     })
  //     .catch(error => {
  //       document.getElementById('verification-result').textContent = "An error occurred.";
  //       console.error('Error:', error);
  //     });
  // });

const nav_sections={"overview":"data","matches":"matches"}
var activeSection=null;

function showpage(){
  console.log("showpage");
  const activePageItem = document.querySelector('.page-item.active');
  const pageLink = activePageItem.querySelector('.page-link');
  const pageValue = pageLink.textContent.trim();
  let table = document.getElementsByClassName('match-list-item')[0];
  table.style.display = 'flex';
  console.log(table);
  //only show 10 items per page
  for (let index = 0; index < table.rows.length; index++) { 
    let item=table.rows[index];
    if (index < pageValue * 10 && index >= (pageValue - 1) * 10) {
      item.style.display = 'block';
    } else {
      item.style.display = 'none';
    }
  }
}



async function showSection() {
    // Get the current hash from the URL
    const hash = window.location.hash;
    const player=JSON.parse(sessionStorage.getItem('player'));
    const playerName = player.playerName;
    const sections = document.querySelectorAll('.section');
    document.getElementById("avatar").src=player.avatar;
    document.getElementById("personaname").innerHTML=player.personaname;
    document.getElementById("profilelink").href=player.profileurl;

    // Hide all sections
    sections.forEach(section => section.classList.remove('active'));
    var html_content;
    // If a valid hash exists, show the matching section
    if (hash) {
        activeSection = document.querySelector(hash);
        if (activeSection) {
            activeSection.classList.add('active');
            console.log(activeSection.id);
            await fetch('get_stats?account_id=' + playerName+"&specific_attr="+nav_sections[activeSection.id],
            {
              method: 'GET',
              headers: {
                application: 'application/json',
              },
            }).then(response => response.json()).then(data => {
              html_content=data.html;
              document.getElementsByClassName("pagination")[0].innerHTML=data.pages
            })
            
        }
        if (activeSection.id=="matches"){

          function updateActivePage(page) {
            // Remove active class from all items
            pageItems.forEach(item => item.classList.remove('active'));
          
            // Add active class to the selected page
            const newActive = pagination.querySelector(`.page-item:nth-child(${page + 1})`);
            newActive.classList.add('active');
          
            // Enable/disable "Previous" and "Next" buttons
            pageItems[0].classList.toggle('disabled', page === 1); // Disable "Previous" on first page
            pageItems[pageItems.length - 1].classList.toggle('disabled', page === pageItems.length - 2); // Disable "Next" on last page
          }

          document.getElementById("matches-list").innerHTML=html_content;
          const pagination = document.getElementsByClassName('pagination')[0];
          console.log(pagination);
          var pageItems = pagination.querySelectorAll('.page-item');
                   
          pagination.addEventListener('click', (e) => {
            e.preventDefault(); // Prevent default anchor behavior
          
            const target = e.target.closest('.page-link');
            if (!target) return;
          
            const pageText = target.textContent.trim();
          
            // Handle "Previous" and "Next" logic
            const activePage = pagination.querySelector('.page-item.active');
            let currentPage = parseInt(activePage.textContent.trim(), 10);
          
            if (pageText === 'Previous' && currentPage > 1) {
                currentPage--;
            } else if (pageText === 'Next' && currentPage < pageItems.length - 2) {
                currentPage++;
            } else if (!isNaN(pageText)) {
                currentPage = parseInt(pageText, 10);
            }
          //   // Update the active page
            updateActivePage(currentPage);
            showpage();
          });
          showpage();
        }
    }
}


window.addEventListener('hashchange', showSection);
window.addEventListener('DOMContentLoaded', showSection);
