document.addEventListener("DOMContentLoaded", function () {
    fetch('output.json')
        .then(response => response.json())
        .then(data => {
            const schedulesContainer = document.getElementById('schedules');

            data.forEach(scheduleData => {
                const scheduleDiv = document.createElement('div');
                scheduleDiv.classList.add('schedule-container');

                const scheduleTitle = document.createElement('h2');
                scheduleTitle.textContent = scheduleData.scheduleName;

                const daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

                daysOfWeek.forEach(dayName => {
                    const dayDiv = document.createElement('div');
                    dayDiv.classList.add('day');

                    const dayHeader = document.createElement('div');
                    dayHeader.classList.add('day-header');
                    dayHeader.textContent = dayName;

                    const dayData = scheduleData.scheduleData.filter(item => item[1] === dayName);

                    if (dayData.length > 0) {
                        dayData.forEach(classData => {
                            const className = classData[0];
                            const eventTimes = classData[2];

                            const eventBlock = document.createElement('div');
                            eventBlock.classList.add('event-block');

                            const classDiv = document.createElement('div');
                            classDiv.classList.add('class-name');
                            classDiv.textContent = className;
                            eventBlock.appendChild(classDiv);

                            eventTimes.forEach(eventTime => {
                                const eventDiv = document.createElement('div');
                                eventDiv.classList.add('event');
                                const startTime = eventTime;
                                const endTime = eventTime + 15; // Assuming classes last for 15 minutes
                                eventDiv.textContent = `${militaryToReadableTime(startTime)} - ${militaryToReadableTime(endTime)}`;
                                eventBlock.appendChild(eventDiv);
                            });

                            dayDiv.appendChild(dayHeader);
                            dayDiv.appendChild(eventBlock);
                        });
                    }

                    scheduleDiv.appendChild(dayDiv);
                });

                schedulesContainer.appendChild(scheduleTitle);
                schedulesContainer.appendChild(scheduleDiv);
            });
        })
        .catch(error => console.error('Error fetching schedule data:', error));

    // Function to convert military time to readable time format
    function militaryToReadableTime(militaryTime) {
        const hours = Math.floor(militaryTime / 100);
        const minutes = militaryTime % 100;
        const period = hours < 12 ? 'AM' : 'PM';
        const formattedHours = hours % 12 === 0 ? 12 : hours % 12;
        return `${formattedHours}:${minutes < 10 ? '0' : ''}${minutes} ${period}`;
    }
});
