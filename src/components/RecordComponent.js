import React, { useState, useRef, useEffect } from 'react';

const mimeType = 'audio/webm';

const RecordComponent = () => {
 const [allowRecording, setAllowRecording] = useState(false);
 // holds the data from creating a new MediaRecorder object given a MediaStream to record
 const mediaRecorder = useRef(null);
 // the stream recieved from the getUserMedia method
 const [audioStream, setAudioStream] = useState(null);
 // inactive, recording, paused
 const [recordingStatus, setRecordingStatus] = useState('inactive');
 // encoded pieces (chunks) of the audio recording
 const [audioChunks, setAudioChunks] = useState([]);
 // blob url to the finished audio recording
 const [audio, setAudio] = useState(null);

 const getMicrophoneAccess = async () => {
  try {
   const streamData = await navigator.mediaDevices.getUserMedia({
    audio: true,
    video: false
   });
   setAllowRecording(true);
   setAudioStream(streamData);
  } catch (err) {
   console.log(`got an error: ${err} while trying to access microphone`);
  }
 };

 const startRecording = async () => {
  setRecordingStatus('recording');
  const media = new MediaRecorder(audioStream, { type: mimeType });
  mediaRecorder.current = media;
  mediaRecorder.current.start();
  let localAudioChunks = [];
  mediaRecorder.current.ondataavailable = (event) => {
   if (typeof event.data === 'undefined') return;
   if (event.data.size === 0) return;
   localAudioChunks.push(event.data);
  };
  setAudioChunks(localAudioChunks);
 };

 const stopRecording = () => {
  setRecordingStatus('inactive');
  mediaRecorder.current.stop();
  mediaRecorder.current.onstop = () => {
   // creates a blob file from the audiochunks data
   const audioBlob = new Blob(audioChunks, { type: mimeType });
   // creates a playable Url from the blob file
   const audioUrl = URL.createObjectURL(audioBlob);
   setAudio(audioUrl);
   setAudioChunks([]);
  };
 };

 return (
  <div>
   {!allowRecording ? (
    <button
     onClick={() => getMicrophoneAccess()}
     className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    >
     Allow Microphone Access
    </button>
   ) : null}
   {allowRecording && recordingStatus === 'inactive' ? (
    <button
     onClick={() => startRecording()}
     className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    >
     Record
    </button>
   ) : null}
   {recordingStatus === 'recording' ? (
    <button
     onClick={() => stopRecording()}
     className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    >
     Stop recording
    </button>
   ) : null}
   {audio ? (
    <div className="audio-container">
     <audio src={audio} controls></audio>
     <a download href={audio}>
      Download Recording
     </a>
    </div>
   ) : null}
  </div>
 );
};

export default RecordComponent;
