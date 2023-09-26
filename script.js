document.addEventListener("DOMContentLoaded", function () {
    // Fetch schedule data from 'output.json'
    fetch('output.json')
        .then(response => response.json())
        .then(data => {
            // Get the schedules container element
            const schedulesContainer = document.getElementById('schedules');

            // Loop through each schedule in the data
            data.forEach(scheduleData => {
                // Create a div for the schedule
                const scheduleDiv = createScheduleDiv(scheduleData);
                // Append the schedule div to the schedules container
                schedulesContainer.appendChild(scheduleDiv);
            });
        })
        .catch(error => console.error('Error fetching schedule data:', error));


    // Function to create a schedule div based on the schedule data
    function createScheduleDiv(scheduleData) {
        // Create a div for the schedule
        const scheduleDiv = document.createElement('div');
        scheduleDiv.classList.add('schedule-container');

        // Create a title for the schedule
        const scheduleTitle = document.createElement('h2');
        scheduleTitle.textContent = scheduleData.scheduleName;
        scheduleDiv.appendChild(scheduleTitle);

        // Define the days of the week
        const daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

        // Loop through each day of the week
        daysOfWeek.forEach(dayName => {
            // Filter the data for the current day
            const dayData = scheduleData.scheduleData.filter(item => item[1] === dayName);

            // if monday show  the word monday/wednesday if tuesday show the word tuesday/thursday 
            // if (dayName === "Monday") {
            //     const dayHeader = document.createElement('div');
            //     dayHeader.classList.add('day-header');
            //     dayHeader.textContent = "Monday/Wednesday";
            //     scheduleDiv.appendChild(dayHeader);
            // }
            // if (dayName === "Tuesday") {
            //     const dayHeader = document.createElement('div');
            //     dayHeader.classList.add('day-header');
            //     dayHeader.textContent = "Tuesday/Thursday";
            //     scheduleDiv.appendChild(dayHeader);
            // }

            


            if (dayData.length > 0) {
                // Create a div for the day
                const dayDiv = document.createElement('div');
                dayDiv.classList.add('day');

                // Create a header for the day
                const dayHeader = document.createElement('div');
                dayHeader.classList.add('day-header');
                dayHeader.textContent = dayName;
                dayDiv.appendChild(dayHeader);

                // Initialize arrays for class names and time blocks
                const classBlocks = [];

                // Loop through class data for the current day
                dayData.forEach(classData => {
                    const className = classData[0];
                    const eventTimes = classData[2];
                    classBlocks.push([className, eventTimes]);
                });

                // Sort the class blocks by start time
                classBlocks.sort((a, b) => a[1][0] - b[1][0]);

                // Create a div for each class
                classBlocks.forEach(classBlock => {
                    const classDiv = document.createElement('div');
                    classDiv.classList.add('class');

                    // Create a div for class name and time
                    const classInfoDiv = document.createElement('div');
                    classInfoDiv.classList.add('class-info');

                    // Create a div for the class name
                    const classNameDiv = document.createElement('div');
                    classNameDiv.classList.add('class-name');
                    classNameDiv.textContent = classBlock[0];
                    classInfoDiv.appendChild(classNameDiv);

                    // Create a div for the time block
                    const timeBlockDiv = document.createElement('div');
                    timeBlockDiv.classList.add('time-block');
                    timeBlockDiv.textContent = createTimeBlockString([classBlock[1]]);
                    classInfoDiv.appendChild(timeBlockDiv);

                    classDiv.appendChild(classInfoDiv);
                    dayDiv.appendChild(classDiv);
                });

                // Append the day div to the schedule div
                scheduleDiv.appendChild(dayDiv);
            }
        });

        return scheduleDiv;
    }

    // Function to create a formatted time block string
    function createTimeBlockString(timeBlocks) {
        return timeBlocks.map(block => {
            const startTime = block[0];
            const endTime = block[block.length - 1] + 15; // Assuming classes last for 15 minutes
            return `${militaryToReadableTime(startTime)} - ${militaryToReadableTime(endTime)}`;
        }).join(', ');
    }

    // Function to convert military time to readable time format
    function militaryToReadableTime(militaryTime) {
        const hours = Math.floor(militaryTime / 100);
        const minutes = militaryTime % 100;
        const period = hours < 12 ? 'AM' : 'PM';
        const formattedHours = hours % 12 === 0 ? 12 : hours % 12;
        return `${formattedHours}:${minutes < 10 ? '0' : ''}${minutes} ${period}`;
    }
});