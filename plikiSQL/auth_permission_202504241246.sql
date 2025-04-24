INSERT INTO public.auth_permission (name,content_type_id,codename) VALUES
	 ('Can add log entry',1,'add_logentry'),
	 ('Can change log entry',1,'change_logentry'),
	 ('Can delete log entry',1,'delete_logentry'),
	 ('Can view log entry',1,'view_logentry'),
	 ('Can add permission',2,'add_permission'),
	 ('Can change permission',2,'change_permission'),
	 ('Can delete permission',2,'delete_permission'),
	 ('Can view permission',2,'view_permission'),
	 ('Can add group',3,'add_group'),
	 ('Can change group',3,'change_group');
INSERT INTO public.auth_permission (name,content_type_id,codename) VALUES
	 ('Can delete group',3,'delete_group'),
	 ('Can view group',3,'view_group'),
	 ('Can add user',4,'add_user'),
	 ('Can change user',4,'change_user'),
	 ('Can delete user',4,'delete_user'),
	 ('Can view user',4,'view_user'),
	 ('Can add content type',5,'add_contenttype'),
	 ('Can change content type',5,'change_contenttype'),
	 ('Can delete content type',5,'delete_contenttype'),
	 ('Can view content type',5,'view_contenttype');
INSERT INTO public.auth_permission (name,content_type_id,codename) VALUES
	 ('Can add session',6,'add_session'),
	 ('Can change session',6,'change_session'),
	 ('Can delete session',6,'delete_session'),
	 ('Can view session',6,'view_session'),
	 ('Can add customer',7,'add_customer'),
	 ('Can change customer',7,'change_customer'),
	 ('Can delete customer',7,'delete_customer'),
	 ('Can view customer',7,'view_customer'),
	 ('Can add product',8,'add_product'),
	 ('Can change product',8,'change_product');
INSERT INTO public.auth_permission (name,content_type_id,codename) VALUES
	 ('Can delete product',8,'delete_product'),
	 ('Can view product',8,'view_product'),
	 ('Can add order',9,'add_order'),
	 ('Can change order',9,'change_order'),
	 ('Can delete order',9,'delete_order'),
	 ('Can view order',9,'view_order'),
	 ('Can add order item',10,'add_orderitem'),
	 ('Can change order item',10,'change_orderitem'),
	 ('Can delete order item',10,'delete_orderitem'),
	 ('Can view order item',10,'view_orderitem');
INSERT INTO public.auth_permission (name,content_type_id,codename) VALUES
	 ('Can add shipping address',11,'add_shippingaddress'),
	 ('Can change shipping address',11,'change_shippingaddress'),
	 ('Can delete shipping address',11,'delete_shippingaddress'),
	 ('Can view shipping address',11,'view_shippingaddress');
