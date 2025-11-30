// Array to store tasks locally (can be replaced with API calls)
let taskList = [];

// Get references to HTML elements
const taskForm = document.getElementById('taskForm');
const taskListUI = document.getElementById('taskList');
const analyzeBtn = document.getElementById('analyzeBtn');

// ----------------------
// Add Task
// ----------------------
taskForm.addEventListener('submit', async (e) => {
  e.preventDefault(); // Prevent the form from reloading the page

  // Get values from the form
  const title = document.getElementById('title').value;
  const due_date = document.getElementById('due_date').value;
  const estimated_hours = parseInt(document.getElementById('estimated_hours').value);
  const importance = parseInt(document.getElementById('importance').value);

  // Create a task object
  const task = { title, due_date, estimated_hours, importance };

  // ----------------------
  // If using API, POST task to backend
  // ----------------------
  /*
  try {
    const response = await fetch('https://your-api.com/tasks', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(task)
    });
    if(response.ok){
      console.log('Task added to backend successfully');
    }
  } catch (error) {
    console.error('Error adding task to backend:', error);
  }
  */

  // For now, push task locally
  taskList.push(task);

  // Reset the form
  taskForm.reset();

  // Display tasks on the page
  displayTasks(taskList);
});

// ----------------------
// Display Tasks
// ----------------------
function displayTasks(tasks) {
  // Clear existing tasks
  taskListUI.innerHTML = '';

  // Loop through each task and display it
  tasks.forEach((task, index) => {
    const li = document.createElement('li');
    li.innerHTML = `
      <strong>${task.title}</strong> 
      | Due: ${task.due_date} 
      | Hours: ${task.estimated_hours} 
      | Importance: ${task.importance}
    `;
    taskListUI.appendChild(li);
  });
}

// ----------------------
// Analyze Tasks
// ----------------------
/*analyzeBtn.addEventListener('click', () => {
  // Copy taskList and sort by importance (high to low) and due date (earliest first)
  const analyzed = [...taskList].sort((a, b) => {
    // Sort by importance first
    if(b.importance !== a.importance) return b.importance - a.importance;

    // If importance is same, sort by due date
    return new Date(a.due_date) - new Date(b.due_date);
  });

  // Display the sorted tasks
  displayTasks(analyzed);
});*/
analyzeBtn.addEventListener('click', () => {
  
  let tempList = [...taskList];  // copy list
  let analyzed = [];

  while (tempList.length > 0) {
    let bestIndex = 0;

    for (let i = 1; i < tempList.length; i++) {
      let current = tempList[i];
      let best = tempList[bestIndex];

      // Compare importance first
      if (current.importance > best.importance) {
        bestIndex = i;
      }

      // If importance same → compare date
      else if (current.importance === best.importance) {
        if (new Date(current.due_date) < new Date(best.due_date)) {
          bestIndex = i;
        }
      }
    }

    // Add best task to analyzed list
    analyzed.push(tempList[bestIndex]);

    // Remove it from temp
    tempList.splice(bestIndex, 1);
  }

  displayTasks(analyzed);
});

// ----------------------
// Optional: Load tasks from API on page load
// ----------------------
/*
async function loadTasksFromAPI() {
  try {
    const response = await fetch('https://your-api.com/tasks');
    const tasksFromAPI = await response.json();
    taskList = tasksFromAPI; // Replace local list with API data
    displayTasks(taskList);
  } catch (error) {
    console.error('Error fetching tasks from API:', error);
  }
}

// Uncomment to load tasks when page loads
// window.onload = loadTasksFromAPI;
*/
