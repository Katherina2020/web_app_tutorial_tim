function deleteNote(noteId){
    // fetch - make a request
    fetch("/delete-note", {
        method: "POST",
        // convert noteId into string
        body: JSON.stringify({ noteId: noteId}),
    }).then((_res) => {
        // when he get a request from /delete-note he will reload the window with GET request 
        window.location.href = "/";
    });

}