import React, { useState } from 'react';
import { Button, Form, Input, message, Modal } from 'antd';
import { SearchOutlined } from '@ant-design/icons';

const CustomSearch=({key='', doSearch})=>{

  const [search, setSearch] = useState(key)
  const [displayModal, setDisplayModal] = useState(false);

  const onSearch = ()=>{
    doSearch(search)
  }


    return  <>
             <Button shape="round" onClick={()=>setDisplayModal(true)} icon={<SearchOutlined />} style={{ marginLeft: '20px', marginTop: '20px'}}>
               Search </Button>
             <Modal
              title="Search"
              visible={displayModal}
              onCancel={()=>setDisplayModal(false)}
              footer={null}
            >
              <Form
                name="company_search"
                
              >
                <Form.Item
                  name="company_name"
                  rules={[{ required: true, message: 'Please Enter' }]}
                >
                  <Input value={search} onChange={(e)=>setSearch(e.target.value)} placeholder="Name" />
                </Form.Item>
     
                <Form.Item>
                  <Button onClick={onSearch} type="primary" htmlType="submit">
                    Search</Button>
                </Form.Item>
              </Form>
            </Modal>
          </>


}
 
export default CustomSearch;
