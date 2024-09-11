/**
 * Removes duplicate tracks from a playlist.
 *
 * @param {string[]} playlist
 * @returns {string[]} new playlist with unique entries
 */
export function removeDuplicates(playlist) {
    const list = new Set(playlist);
    let arr = [...list]
    return arr
  }
  
  /**
   * Checks whether a playlist includes a track.
   *
   * @param {string[]} playlist
   * @param {string} track
   * @returns {boolean} whether the track is in the playlist
   */
  export function hasTrack(playlist, track) {
    return playlist.includes(track)
  }
  
  /**
   * Adds a track to a playlist.
   *
   * @param {string[]} playlist
   * @param {string} track
   * @returns {string[]} new playlist
   */
  export function addTrack(playlist, track) {
    if(playlist.includes(track)) {
      return playlist
    }else {
      playlist.push(track)
      return playlist
    }
  }
  
  /**
   * Deletes a track from a playlist.
   *
   * @param {string[]} playlist
   * @param {string} track
   * @returns {string[]} new playlist
   */
  export function deleteTrack(playlist, track) {
    for (let i = 0; i < playlist.length; i++) {
      if (playlist[i] === track) {
        playlist.splice(i, 1);
        return playlist;
      }
    }
    return playlist;
  }
  
  /**
   * Lists the unique artists in a playlist.
   *
   * @param {string[]} playlist
   * @returns {string[]} list of artists
   */
  export function listArtists(playlist) {
    let artistsSet = new Set();
    
    for (let track of playlist) {
      let artist = track.split(' - ')[1];
      artistsSet.add(artist);
    }
  
    return Array.from(artistsSet);
  }