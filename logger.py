create or replace function py_logger()
returns trigger as $$
     # if int(TD['new']['id'])%2 == 0:
     tx_id = plpy.execute('SELECT txid_current() AS tx_id')[0]['tx_id']
     table_name = TD.get('table_name')
     event = TD.get('event')
     old_content = TD.get('old') and str(TD.get('old')) or ''
     if old_content != '':
         create_date = TD.get('old').get('create_date')
         res_id = TD.get('old').get('id')
         create_uid = TD.get('old').get('create_uid')
     else:
         create_date = TD.get('new').get('create_date')
         res_id = TD.get('new').get('id')
         create_uid = TD.get('new').get('create_uid')
     new_content = TD.get('new') and str(TD.get('new')) or ''
     model_name = table_name.replace('_','.')
     model_id = plpy.execute("SELECT id AS model_id from ir_model where model = '%s'"%(model_name))[0]['model_id']
     qty = plpy.execute("SELECT COUNT(*) AS qty FROM DATA_LOGGER WHERE EVENT = '%s' and TX_ID = %s"%(TD.get('event'),tx_id))[0]['qty']
     if qty == 0:
         #sql_statement = 'INSERT INTO data_logger(table_name,event,old_content,new_content) VALUES ("%s","%s","%s","%s")'%(table_name,event,old_content,new_content)
         sql = plpy.prepare(""" INSERT INTO data_logger(table_name, event, old_content, new_content, model_id, create_date, res_id, tx_id, create_uid) values ($1, $2, $3, $4, $5, $6, $7, $8
, $9); """,\
             ("TEXT", "TEXT", "TEXT", "TEXT", "INTEGER", "TIMESTAMP","INTEGER","INTEGER","INTEGER"))
         #sql = plpy.prepare(sql_statement)
         ss = plpy.execute(sql, (TD['table_name'], TD['event'],TD['old'], TD['new'], model_id, create_date, res_id, tx_id, create_uid))
         #ss = plpy.execute(sql)
$$ language plpython3u;
