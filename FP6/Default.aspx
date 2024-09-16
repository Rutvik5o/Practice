<%@ Page Language="C#" AutoEventWireup="true"  CodeFile="Default.aspx.cs" Inherits="_Default" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Untitled Page</title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        <br />
        <br />
        <br />
        <asp:TextBox ID="TextBox1" runat="server" Width="257px"></asp:TextBox>
    
    </div>
    <asp:Literal ID="Literal1" runat="server"></asp:Literal>
    <p>
        <asp:Button ID="Button1" runat="server" onclick="Button1_Click" 
            Text="Click here for change title bar" />
    </p>
    </form>
</body>
</html>
