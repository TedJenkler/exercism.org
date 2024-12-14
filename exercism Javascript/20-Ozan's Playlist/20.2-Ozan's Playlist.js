export function removeDuplicates(playlist) {
    let mySet = new Set(playlist)
    return Array.from(mySet)
  }
  
  export function hasTrack(playlist, track) {
    return playlist.includes(track)
  }
  
  export function addTrack(playlist, track) {
    playlist.push(track)
    let mySet = new Set(playlist)
    return Array.from(mySet)
  }
  
  export function deleteTrack(playlist, track) {
    return playlist.filter((item) => item != track)
  }
  
  export function listArtists(playlist) {
    let artists = []
    for (let item of playlist) {
      const [_, artist] = item.split(" - ")
      artists.push(artist)
    }
    let mySet = new Set(artists)
    return Array.from(mySet)
  }