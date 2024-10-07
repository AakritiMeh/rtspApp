import  { useState, useEffect } from 'react';
import axios from 'axios';
//import ReactPlayer from 'react-player';

function App() {
  const [streamUrl, setStreamUrl] = useState('');
  const [overlays, setOverlays] = useState([]);
  const [overlaySettings, setOverlaySettings] = useState({
    position: { top: '10px', left: '10px' },
    size: { width: '100px', height: '100px' },
    content: 'Sample Overlay',
  });

  useEffect(() => {
    // Fetch the stream URL
    axios.get('http://localhost:5000/stream')
      .then(res => setStreamUrl(res.data.rtsp_url))
      .catch(err => console.error(err));

    // Fetch overlay settings
    axios.get('http://localhost:5000/overlays')
      .then(res => setOverlays(res.data))
      .catch(err => console.error(err));
  }, []);

  const handleOverlayUpdate = () => {
    axios.put(`http://localhost:5000/overlays/${overlaySettings._id}`, overlaySettings)
      .then(res => console.log(res.data))
      .catch(err => console.error(err));
  };

  const renderOverlay = (overlay) => (
    <div
      key={overlay._id}
      style={{
        position: 'absolute',
        top: overlay.position.top,
        left: overlay.position.left,
        width: overlay.size.width,
        height: overlay.size.height,
      }}
    >
      {overlay.content}
    </div>
  );

  return (
    <div>
      <h1>Live Stream with Overlay</h1>
      <iframe
        src={streamUrl}        
        allow='autoplay; encrypted-media'
        allowfullscreen
        title='video'
        width="800"
        height="100"
      />
      {/* <ReactPlayer url={streamUrl} playing controls width="100%" height="auto" /> */}
      <div className="overlay-container">
        {overlays.map(renderOverlay)}
      </div>

      <div className="overlay-settings">
        <input
          type="text"
          value={overlaySettings.content}
          onChange={e => setOverlaySettings({ ...overlaySettings, content: e.target.value })}
          placeholder="Overlay Content"
        />
        <button onClick={handleOverlayUpdate}>Update Overlay</button>
      </div>
    </div>
  );
}

export default App;
