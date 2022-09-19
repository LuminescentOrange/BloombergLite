const SERVER_ORIGIN = '';
 
const loginUrl = `${SERVER_ORIGIN}/login`;
 
export const login = (credential) => {
  return fetch(loginUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    credentials: 'include',
    body: JSON.stringify(credential)
  }).then((response) => {
    if (response.status !== 200) {
      throw Error('Fail to log in');
    }
 
    return response.json();
  })
}
 

const logoutUrl = `${SERVER_ORIGIN}/logout`;
 
export const logout = () => {
  return fetch(logoutUrl, {
    method: 'POST',
    credentials: 'include',
  }).then((response) => {
    if (response.status !== 200) {
      throw Error('Fail to log out');
    }
  })
}

//register
const registerUrl = `${SERVER_ORIGIN}/register`;
 
export const register = (data) => {
  return fetch(registerUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
  }).then((response) => {
    if (response.status !== 200) {
      throw Error('Fail to register');
    }
  })
}

// const getDetails = (symbol) => {
//   return fetch(`${SERVER_ORIGIN}//lookup/earning/${symbol}`).then((response) => {
//     if (response.status !== 200) {
//       throw Error('Fail to find');
//     }
 
//     return response.json();
//   });
// }

// export const searchCompany = (symbol) => {
//   return getDetails(symbol).then((data) => {
//     if (data && data.id) {
//       return searchCompany(data);
//     }
 
//     throw Error('Fail to find')
//   })
// }
