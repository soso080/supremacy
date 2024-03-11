// create Agora client
var client = AgoraRTC.createClient({
  mode: "rtc",
  codec: "vp8"
});
var localTracks = {
  videoTrack:null,
  audioTrack: null,
  audioTrack: null,
  audioEffectTrack: null
};

var localTrackState = {
  videoTrackMuted: false,
  audioTrackMuted: false
};
var remoteUsers = {};
// Agora client options
var options = {
  appid: null,
  channel: null,
  uid: null,
  token: null
};
var audioMixing = {
  state: "IDLE",
  // "IDLE" | "LOADING | "PLAYING" | "PAUSE"
  duration: 0
};
const playButton = $(".play");
let audioMixingProgressAnimation;

// the demo can auto join channel with params in url
$(() => {
  var urlParams = new URL(location.href).searchParams;
  options.appid = urlParams.get("appid");
  options.channel = urlParams.get("channel");
  options.token = urlParams.get("token");
  options.uid = urlParams.get("uid");
  if (options.appid && options.channel) {
    $("#uid").val(options.uid);
    $("#appid").val(options.appid);
    $("#token").val(options.token);
    $("#channel").val(options.channel);
    $("#join-form").submit();
  }
});



$("#mute-audio").click(async function  (e) {
  
    await muteAudio();
});

$("#unmute-audio").click(async function  (e) {
    await unmuteAudio();
});

$("#resume").click(function  (e) {
  resume();
});

$("#pause").click(function  (e) {
  pause();
});

$("#join-form").submit(async function (e) {
  e.preventDefault();
  $("#join").attr("disabled", true);
  try {
    options.channel = $("#channel").val();
    options.uid = Number($("#uid").val());
    options.appid = $("#appid").val();
    options.token = $("#token").val();
    await join();
    if (options.token) {
      $("#success-alert-with-token").css("display", "block");
    } else {
      $("#success-alert a").attr("href", `index.html?appid=${options.appid}&channel=${options.channel}&token=${options.token}`);
      $("#success-alert").css("display", "block");
    }
  } catch (error) {
    console.error(error);
  } finally {
    $("#leave").attr("disabled", false);
    $("#audio-mixing").attr("disabled", false);
    $("#audio-effect").attr("disabled", false);
    $("#stop-audio-mixing").attr("disabled", false);
    $("#local-audio-mixing").attr("disabled", false);
  }
});
$("#leave").click(async function (e) {
  leave();
});
$("#audio-mixing").click(function (e) {
  startAudioMixing();
});
$("#audio-effect").click(async function (e) {
  // play the audio effect
  await playEffect(1, {
    source: "audio.mp3"
  });
  console.log("play audio effect success");
});
$("#stop-audio-mixing").click(function (e) {
  stopAudioMixing();
  return false;
});
$(".audio-bar .progress").click(function (e) {
  setAudioMixingPosition(e.offsetX);
  return false;
});
$("#volume").click(function (e) {
  setVolume($("#volume").val());
});
$("#local-audio-mixing").click(function (e) {
  // get selected file
  const file = $("#local-file").prop("files")[0];
  if (!file) {
    console.warn("please choose a audio file");
    return;
  }
  startAudioMixing(file);
  return false;
});
playButton.click(function () {
  if (audioMixing.state === "IDLE" || audioMixing.state === "LOADING") return;
  toggleAudioMixing();
  return false;
});
function setAudioMixingPosition(clickPosX) {
  if (audioMixing.state === "IDLE" || audioMixing.state === "LOADING") return;
  const newPosition = clickPosX / $(".progress").width();

  // set the audio mixing playing position
  localTracks.audioTrack.seekAudioBuffer(newPosition * audioMixing.duration);
}
function setVolume(value) {
  // set the audio mixing playing position
  localTracks.audioTrack.setVolume(parseInt(value));
  console.log(value);
}
async function startAudioMixing(file) {
  if (audioMixing.state === "PLAYING" || audioMixing.state === "LOADING") return;
  const options = {};
  if (file) {
    options.source = file;
  } else {
    options.source = "HeroicAdventure.mp3";
  }
  try {
    audioMixing.state = "LOADING";
    // if the published track will not be used, you had better unpublish it
    if (localTracks.audioTrack) {
      await client.unpublish(localTracks.audioTrack);
    }
    // start audio mixing with local file or the preset file
    localTracks.audioTrack = await AgoraRTC.createBufferSourceAudioTrack(options);
    await client.publish(localTracks.audioTrack);
    localTracks.audioTrack.play();
    localTracks.audioTrack.startProcessAudioBuffer({
      loop: true
    });
    audioMixing.duration = localTracks.audioTrack.duration;
    $(".audio-duration").text(toMMSS(audioMixing.duration));
    playButton.toggleClass('active', true);
    setAudioMixingProgress();
    audioMixing.state = "PLAYING";
    console.log("start audio mixing");
  } catch (e) {
    audioMixing.state = "IDLE";
    console.error(e);
  }
}
function stopAudioMixing() {
  if (audioMixing.state === "IDLE" || audioMixing.state === "LOADING") return;
  audioMixing.state = "IDLE";

  // stop audio mixing track
  localTracks.audioTrack.stopProcessAudioBuffer();
  localTracks.audioTrack.stop();
  $(".progress-bar").css("width", "0%");
  $(".audio-current-time").text(toMMSS(0));
  $(".audio-duration").text(toMMSS(0));
  playButton.toggleClass('active', false);
  cancelAnimationFrame(audioMixingProgressAnimation);
  console.log("stop audio mixing");
}
function resume() {
  localTracks.audioTrack.resumeProcessAudioBuffer();
  audioMixing.state = "PLAYING";
  }
function pause() {
    localTracks.audioTrack.pauseProcessAudioBuffer();
    audioMixing.state = "PAUSE";}


function setProgressBar(percentage) {
      const progressBar = document.getElementById("p-bar");
      progressBar.style.width = `${percentage}%`;
      progressBar.setAttribute("aria-valuenow", percentage);
    }
    

function setAudioMixingProgress() {
  audioMixingProgressAnimation = requestAnimationFrame(setAudioMixingProgress);
  const currentTime = localTracks.audioTrack.getCurrentTime();
  $(".progress-bar").css("width", `${currentTime / audioMixing.duration * 100}%`);
  $(".audio-current-time").text(toMMSS(currentTime));
}

// use buffer source audio track to play effect.
async function playEffect(cycle, options) {
  // if the published track will not be used, you had better unpublish it
  if (localTracks.audioEffectTrack) {
    await client.unpublish(localTracks.audioEffectTrack);
  }
  localTracks.audioEffectTrack = await AgoraRTC.createBufferSourceAudioTrack(options);
  await client.publish(localTracks.audioEffectTrack);
  localTracks.audioEffectTrack.play();
  localTracks.audioEffectTrack.startProcessAudioBuffer({
    cycle
  });
}
async function join() {
  // add event listener to play remote tracks when remote user publishs.
  client.on("user-published", handleUserPublished);
  client.on("user-unpublished", handleUserUnpublished);

  // join a channel and create local tracks, we can use Promise.all to run them concurrently
  [options.uid, localTracks.audioTrack] = await Promise.all([
  // join the channel
  client.join(options.appid, options.channel, options.token || null, options.uid || null),
  // create local tracks, using microphone and camera
  AgoraRTC.createMicrophoneAudioTrack()]);
  // play local video track
  
  

  // publish local tracks to channel
  await client.publish(Object.values(localTracks).filter(track => track !== null));
  console.log("publish success");
  
}
async function leave() {
  stopAudioMixing();
  for (trackName in localTracks) {
    var track = localTracks[trackName];
    if (track) {
      track.stop();
      track.close();
      localTracks[trackName] = null;
    }
  }
  // remove remote users and player views
  remoteUsers = {};
  $("#remote-playerlist").html("");

  // leave the channel
  await client.leave();
  $("#local-player-name").text("");
  $("#join").attr("disabled", false);
  $("#leave").attr("disabled", true);
  $("#audio-mixing").attr("disabled", true);
  $("#audio-effect").attr("disabled", true);
  $("#stop-audio-mixing").attr("disabled", true);
  $("#local-audio-mixing").attr("disabled", true);
  console.log("client leaves channel success");
}
async function subscribe(user, mediaType) {
  const uid = user.uid;
  // subscribe to a remote user
  await client.subscribe(user, mediaType);
  console.log("subscribe success");
  if (mediaType === 'video') {
    const player = $(`
      <div id="player-wrapper-${uid}">
        <p class="player-name">remoteUser(${uid})</p>
        <div id="player-${uid}" class="player"></div>
      </div>
    `);
    $("#remote-playerlist").append(player);
    user.videoTrack.play(`player-${uid}`);
  }
  if (mediaType === 'audio') {
    user.audioTrack.play();
  }
}
function handleUserPublished(user, mediaType) {
  const id = user.uid;
  remoteUsers[id] = user;
  subscribe(user, mediaType);
}
function handleUserUnpublished(user, mediaType) {
  if (mediaType === 'video') {
    const id = user.uid;
    delete remoteUsers[id];
    $(`#player-wrapper-${id}`).remove();
  }
}

async function muteAudio() {
  
  localTracks.audioTrack.setMuted(true);
  
}

async function unmuteAudio() {
  
  localTracks.audioTrack.setMuted(false);

}

// calculate the MM:SS format from millisecond
function toMMSS(second) {
  // const second = millisecond / 1000;
  let MM = parseInt(second / 60);
  let SS = parseInt(second % 60);
  MM = MM < 10 ? "0" + MM : MM;
  SS = SS < 10 ? "0" + SS : SS;
  return `${MM}:${SS}`;
}