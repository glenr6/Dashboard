import { createStore, combineReducers } from 'redux';
import tokenReducer from './reducers/tokenReducer';

const rootReducer = combineReducers({
  // Add your reducers here
  token: tokenReducer,
});

const store = createStore(rootReducer);

export default store;
