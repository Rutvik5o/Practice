<%@ Page Language="C#" AutoEventWireup="true"  CodeFile="Default.aspx.cs" Inherits="_Default" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Untitled Page</title>
    <style type="text/css">
        .style1
        {
            width: 100%;
            height: 157px;
        }
        .style2
        {
            width: 251px;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
    <p>
&nbsp;&nbsp;&nbsp;
        <h1>Select Any Bill Payment Method:</h1>
        <asp:RadioButtonList ID="RadioButtonList1" runat="server" AutoPostBack="True" 
            RepeatDirection="Horizontal" 
        onselectedindexchanged="RadioButtonList1_SelectedIndexChanged">
            <asp:ListItem>By Cash</asp:ListItem>
            <asp:ListItem>By Debit/Credit Card</asp:ListItem>
            <asp:ListItem>By Cheque</asp:ListItem>
        </asp:RadioButtonList>
        </p>
    <asp:Panel ID="Panel1" runat="server" Height="114px" Visible="False">
       <strong> Bill Payment By Cash</strong><br />
        <br />
        Enter Amount -&gt;&nbsp;
        <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
        <br />
        <br />
        <asp:Button ID="Button1" runat="server" onclick="Button1_Click" Text="Submit" />
    </asp:Panel>
        <p>
            &nbsp;</p>
        <asp:Panel ID="Panel2" runat="server" Height="248px" Visible="False">
            <strong>Bill Payment By Credit/Debit Card</strong><br />
            <br />
            <table class="style1">
                <tr>
                    <td class="style2">
                        Enter Card Number-&gt;</td>
                    <td>
                        <asp:TextBox ID="TextBox8" runat="server" Width="428px"></asp:TextBox>
                    </td>
                </tr>
                <tr>
                    <td class="style2">
                        Enter Expiry Date -&gt;</td>
                    <td>
                        <asp:TextBox ID="TextBox9" runat="server" Width="187px"></asp:TextBox>
                    </td>
                </tr>
                <tr>
                    <td class="style2">
                        Enter CVV -&gt;</td>
                    <td>
                        <asp:TextBox ID="TextBox10" runat="server" Width="183px"></asp:TextBox>
                    </td>
                </tr>
                <tr>
                    <td class="style2">
                        Enter Amount-&gt;</td>
                    <td>
                        <asp:TextBox ID="TextBox11" runat="server" Width="179px"></asp:TextBox>
                    </td>
                </tr>
            </table>
            <br />
            <asp:Button ID="Button4" runat="server" onclick="Button4_Click" Text="Submit" />
            <br />
        </asp:Panel>
    <p>
        &nbsp;</p>
    <asp:Panel ID="Panel3" runat="server" Height="193px" Visible="False">
        <strong>Bill Payment By Cheque</strong>
        <br />
        <br />
        <br />
        Enter Cheque Number -&gt;&nbsp;&nbsp;&nbsp;&nbsp;
        <asp:TextBox ID="TextBox6" runat="server" Width="236px"></asp:TextBox>
        <br />
        <br />
        <br />
        Enter Amount-&gt;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <asp:TextBox ID="TextBox7" runat="server" Width="154px"></asp:TextBox>
        &nbsp;&nbsp;&nbsp;
        <br />
        <br />
        <asp:Button ID="Button3" runat="server" Text="Submit" onclick="Button3_Click" />
        <br />
        <br />
    </asp:Panel>
    <p>
    </p>
    </form>
</body>
</html>
