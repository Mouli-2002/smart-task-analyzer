let taskList = [];

const taskForm = document.getElementById('taskForm');
const taskListUI = document.getElementById('taskList');
const analyzeBtn = document.getElementById('analyzeBtn');

// Add Task
taskForm.addEventListener('submit', (e) => {
  e.preventDefault();

  const title = document.getElementById('title').value;
  const due_date = document.getElementById('due_date').value;
  const estimated_hours = parseInt(document.getElementById('estimated_hours').value);
  const importance = parseInt(document.getElementById('importance').value);

  const task = { title, due_date, estimated_hours, importance };
  taskList.push(task);

  taskForm.reset();
  displayTasks(taskList);
});

// Display Tasks
function displayTasks(tasks) {
  taskListUI.innerHTML = '';
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

// Analyze Tasks (simple priority: importance first, then due date)
analyzeBtn.addEventListener('click', () => {
  const analyzed = [...taskList].sort((a, b) => {
    if(b.importance !== a.importance) return b.importance - a.importance;
    return new Date(a.due_date) - new Date(b.due_date);
  });
  displayTasks(analyzed);
});
